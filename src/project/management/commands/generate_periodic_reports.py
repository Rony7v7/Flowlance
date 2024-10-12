from django.core.management.base import BaseCommand
from django.utils import timezone
from project.models import Project, ProjectReportSettings
from django.core.mail import EmailMessage
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from project.models import Project, ProjectReportSettings, Task, Milestone
from datetime import date


class Command(BaseCommand):
    help = 'Generates periodic project reports based on settings'

    def handle(self, *args, **options):
        today = timezone.now().date()
        projects = Project.objects.filter(is_deleted=False)

        for project in projects:
            settings, _ = ProjectReportSettings.objects.get_or_create(project=project)
            
            if self.should_generate_report(settings, today):
                pdf_buffer = self.generate_report(project, settings)
                self.send_report_email(project, pdf_buffer)

    def should_generate_report(self, settings, today):
        if settings.report_frequency == 'daily':
            return True
        elif settings.report_frequency == 'weekly' and today.weekday() == 0:  # Monday
            return True
        elif settings.report_frequency == 'monthly' and today.day == 1:
            return True
        return False

    def generate_report(self, project, settings):
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        
        p.drawString(100, 750, f"Project Report: {project.title}")
        
        y_position = 700
        
        if settings.include_milestone_progress:
            p.drawString(100, y_position, "Milestone Progress")
            y_position -= 20
            milestone_progress = self.calculate_milestone_progress(project)
            p.drawString(120, y_position, f"Overall progress: {milestone_progress:.2f}%")
            y_position -= 40
        
        if settings.include_task_progress:
            p.drawString(100, y_position, "Task Progress")
            y_position -= 20
            task_progress = self.calculate_task_progress(project)
            p.drawString(120, y_position, f"Overall progress: {task_progress:.2f}%")
            y_position -= 40
        
        if settings.include_milestones_and_tasks:
            p.drawString(100, y_position, "Milestones and Tasks")
            y_position -= 20
            for milestone in project.milestones.filter(is_deleted=False):
                p.drawString(120, y_position, f"Milestone: {milestone.name}")
                y_position -= 15
                p.drawString(130, y_position, f"Progress: {milestone.amount_completed}/{milestone.assigments.count()} assignments completed")
                y_position -= 15
                p.drawString(130, y_position, f"Deadline: {milestone.end_date} ({milestone.deadline_color})")
                y_position -= 15
                for task in milestone.tasks.filter(is_deleted=False):
                    p.drawString(140, y_position, f"Task: {task.title} - Status: {task.state}")
                    y_position -= 15
                y_position -= 10
        
        if settings.include_kanban_board:
            p.drawString(100, y_position, "Kanban Board")
            y_position -= 20
            states = ['pendiente', 'En progreso', 'Completada']
            for state in states:
                p.drawString(120, y_position, f"Column: {state}")
                y_position -= 15
                tasks = Task.objects.filter(milestone__project=project, state=state, is_deleted=False)
                for task in tasks:
                    p.drawString(140, y_position, f"Task: {task.title}")
                    y_position -= 15
                y_position -= 10
        
        if settings.include_gantt_chart:
            p.drawString(100, y_position, "Gantt Chart")
            y_position -= 20
            p.drawString(120, y_position, "Gantt chart would be displayed here")
            y_position -= 40
        
        p.showPage()
        p.save()
        buffer.seek(0)
        return buffer

    def calculate_milestone_progress(self, project):
        milestones = project.milestones.filter(is_deleted=False)
        total_milestones = milestones.count()
        if total_milestones == 0:
            return 0

        completed_milestones = sum(
            1 for milestone in milestones
            if milestone.amount_completed == milestone.assigments.count() and milestone.assigments.count() > 0
        )

        return (completed_milestones / total_milestones) * 100

    def calculate_task_progress(self, project):
        tasks = Task.objects.filter(milestone__project=project, is_deleted=False)
        total_tasks = tasks.count()
        completed_tasks = tasks.filter(state='Completada').count()
        return (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
