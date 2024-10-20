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
            client=self.user
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
            end_date=timezone.now().date() + timedelta(days=7)
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
        progress = command.calculate_milestone_progress(self.project)
        self.assertEqual(progress, 0)  # No completed milestones yet

        self.milestone.amount_completed = 1
        self.milestone.save()
        progress = command.calculate_milestone_progress(self.project)
        self.assertEqual(progress, 100)  # All milestones completed

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