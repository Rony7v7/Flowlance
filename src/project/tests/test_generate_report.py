from django.test import TestCase
from django.core.management import call_command
from django.contrib.auth.models import User
from django.utils import timezone
from io import StringIO
from project.management.commands.generate_periodic_reports import Command
from project.models import Project, Milestone, Task, UserProjectReportSettings, ProjectReportSettings
from unittest.mock import patch
from datetime import timedelta

class ReportGenerationCommandTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=30),
            client=self.user,
            budget=10000  # Añadir un valor para el presupuesto (budget)
        )
        self.milestone = Milestone.objects.create(
            name="Test Milestone",
            project=self.project,
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=15)
        )
        self.task = Task.objects.create(
            title="Test Task",
            milestone=self.milestone,
            state="En progreso",
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=7),
            responsible=self.user  # Proporciona un valor para el campo 'responsible'
        )
        self.report_settings = ProjectReportSettings.objects.create(
            project=self.project,
            include_milestone_progress=True,
            include_task_progress=True,
            include_milestones_and_tasks=True,
            include_kanban_board=True,
            include_gantt_chart=True,
            report_frequency='daily'
        )
        self.user_report_settings = UserProjectReportSettings.objects.create(
            user=self.user,
            report_settings=self.report_settings
        )

    @patch('project.management.commands.generate_periodic_reports.Command.send_report_email')
    def test_handle_method(self, mock_send_email):
        out = StringIO()
        call_command('generate_periodic_reports', stdout=out)
        self.assertIn('', out.getvalue())  # Check if command runs without errors
        mock_send_email.assert_called_once()  # Check if email sending was attempted

    def test_should_generate_report(self):
        command = Command()
        self.assertTrue(command.should_generate_report(self.report_settings, timezone.now().date()))
        
        self.report_settings.report_frequency = 'weekly'
        self.report_settings.save()
        self.assertEqual(command.should_generate_report(self.report_settings, timezone.now().date()), 
                         timezone.now().weekday() == 0)

        self.report_settings.report_frequency = 'monthly'
        self.report_settings.save()
        self.assertEqual(command.should_generate_report(self.report_settings, timezone.now().date()), 
                         timezone.now().day == 1)

    def test_calculate_milestone_progress(self):
        command = Command()

        # Progreso inicial debería ser 0
        initial_progress = command.calculate_milestone_progress(self.project)
        self.assertEqual(initial_progress, 0, "El progreso inicial debería ser 0%")

        # Asegúrate de que la tarea existente esté asociada correctamente al hito
        self.task.milestone = self.milestone
        self.task.save()

        # Agrega una segunda tarea al hito
        self.task2 = Task.objects.create(
            title="Second Test Task",
            milestone=self.milestone,
            state="En progreso",
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=7),
            responsible=self.user
        )

        # Verifica que hay dos tareas en el hito
        self.assertEqual(self.milestone.tasks.count(), 2, "Debe haber dos tareas en el hito.")  # Usar 'tasks'

        # Simula la finalización de ambas tareas
        self.task.state = 'Completada'
        self.task.save()
        self.task2.state = 'Completada'
        self.task2.save()

        # Verifica que ambas tareas están completadas
        self.assertEqual(self.milestone.tasks.filter(state='Completada').count(), 2, "Ambas tareas deberían estar completadas.")

        # Recalcula el progreso después de completar las tareas
        progress = command.calculate_milestone_progress(self.project)

        # Verifica que el progreso sea 100%
        self.assertEqual(progress, 100, f"El progreso debería ser 100%, pero es {progress}%")

        # Agrega un nuevo hito incompleto para verificar el cálculo de progreso parcial
        new_milestone = Milestone.objects.create(
            name="New Test Milestone",
            project=self.project,
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=15)
        )
        Task.objects.create(
            title="New Test Task",
            milestone=new_milestone,
            state="En progreso",
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=7),
            responsible=self.user
        )

        # Recalcula el progreso con el nuevo hito incompleto
        final_progress = command.calculate_milestone_progress(self.project)

        # Verifica que el progreso sea 50% (1 de 2 hitos completados)
        self.assertEqual(final_progress, 50, f"El progreso final debería ser 50%, pero es {final_progress}%")



    def test_calculate_task_progress(self):
        command = Command()
        progress = command.calculate_task_progress(self.project)
        self.assertEqual(progress, 0)  # No completed tasks yet

        self.task.state = 'Completada'
        self.task.save()
        progress = command.calculate_task_progress(self.project)
        self.assertEqual(progress, 100)  # All tasks completed

    @patch('project.management.commands.generate_periodic_reports.canvas.Canvas')
    def test_generate_report(self, mock_canvas):
        command = Command()
        buffer = command.generate_report(self.project, self.report_settings)
        self.assertIsNotNone(buffer)
        mock_canvas.assert_called_once()

    @patch('project.management.commands.generate_periodic_reports.EmailMessage')
    def test_send_report_email(self, mock_email):
        command = Command()
        command.send_report_email(self.user, self.project, StringIO())
        mock_email.assert_called_once()
        mock_email.return_value.send.assert_called_once()
