from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from project.models import Project, ProjectReportSettings, UserProjectReportSettings, Task, Milestone
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from django.core.mail import EmailMessage

class Command(BaseCommand):
    help = 'Test sending a project report email to a specific user'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='ID of the user to send the test report')
        parser.add_argument('project_id', type=int, help='ID of the project to generate the report for')

    def handle(self, *args, **options):
        user_id = options['user_id']
        project_id = options['project_id']

        try:
            user = User.objects.get(id=user_id)
            project = Project.objects.get(id=project_id)
        except (User.DoesNotExist, Project.DoesNotExist):
            self.stdout.write(self.style.ERROR('User or Project not found'))
            return

        user_settings, created = UserProjectReportSettings.objects.get_or_create(
            user=user,
            report_settings__project=project,
            defaults={'report_settings': ProjectReportSettings.objects.create(project=project)}
        )
        settings = user_settings.report_settings

        pdf_buffer = self.generate_report(project, settings)
        self.send_report_email(user, project, pdf_buffer)

        self.stdout.write(self.style.SUCCESS(f'Test report sent to {user.email} for project {project.title}'))

    def generate_report(self, project, settings):
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)

        # Colores personalizados
        colors_dict = {
            "bg_white": colors.HexColor("#FAFAFD"),
            "bg_gray": colors.HexColor("#EAEBF9"),
            "primary_lightest": colors.HexColor("#D5D7F2"),
            "primary_black": colors.HexColor("#121670"),
            "primary_light": colors.HexColor("#8D92F2"),
            "primary_medium": colors.HexColor("#636AF2"),
            "primary_dark": colors.HexColor("#3D46F2"),
            "milestone_bg": colors.HexColor("#F0F1FC"),
            "task_complete": colors.HexColor("#4CAF50"),
            "task_inprogress": colors.HexColor("#FFC107"),
            "task_pending": colors.HexColor("#F44336")
        }

        # Dibujar encabezado
        p.setFillColor(colors_dict["primary_medium"])
        p.roundRect(0, 730, 612, 60, 10, fill=True)
        p.setFillColor(colors.white)
        p.setFont("Helvetica-Bold", 22)
        p.drawCentredString(300, 765, f"Project Report: {project.title}")

        y_position = 710  # Posición inicial del contenido

        # Función para dibujar los títulos de sección
        def draw_section_title(title, y_pos, p, colors_dict):
            p.setStrokeColor(colors_dict["primary_lightest"])
            p.setLineWidth(1.5)
            p.setFillColor(colors_dict["primary_dark"])
            p.setFont("Helvetica-Bold", 16)
            p.drawString(50, y_pos, title)
            return y_pos - 30

        # Milestone Progress
        if settings.include_milestone_progress:
            y_position = draw_section_title("Milestone Progress", y_position, p, colors_dict)
            p.setFont("Helvetica", 12)
            p.setFillColor(colors.black)
            milestone_progress = self.calculate_milestone_progress(project)
            p.drawString(70, y_position, f"Overall progress: {milestone_progress:.2f}%")
            y_position -= 50

        # Task Progress
        if settings.include_task_progress:
            y_position = draw_section_title("Task Progress", y_position, p, colors_dict)
            task_progress = self.calculate_task_progress(project)
            p.setFont("Helvetica", 12)
            p.setFillColor(colors.black)
            p.drawString(70, y_position, f"Overall progress: {task_progress:.2f}%")
            y_position -= 50

        # Milestones and Tasks
        if settings.include_milestones_and_tasks:
            y_position = draw_section_title("Milestones and Tasks", y_position, p, colors_dict)

            for milestone in project.milestones.filter(is_deleted=False):
                # Calcular la altura del bloque del milestone
                num_tasks = milestone.tasks.filter(is_deleted=False).count()
                block_height = 80 + (num_tasks * 15)

                # Dibujar fondo del milestone
                p.setFillColor(colors_dict["milestone_bg"])
                p.roundRect(50, y_position - block_height, 500, block_height, 5, fill=True, stroke=False)

                # Título del milestone
                p.setFont("Helvetica-Bold", 12)
                p.setFillColor(colors_dict["primary_dark"])
                p.drawString(70, y_position - 30, f"Milestone: {milestone.name}")

                # Detalles del milestone
                p.setFont("Helvetica", 10)
                p.setFillColor(colors.black)
                p.drawString(70, y_position - 45, f"Progress: {milestone.amount_completed}/{milestone.assigments.count()} assignments completed")
                p.drawString(70, y_position - 60, f"Deadline: {milestone.end_date}")

                # Indicador del estado del milestone
                status_color = colors_dict["task_complete"] if milestone.amount_completed == milestone.assigments.count() else colors_dict["task_inprogress"]
                p.setFillColor(status_color)
                p.circle(520, y_position - 50, 5, fill=True)

                # Listar tareas dentro del milestone
                task_y_position = y_position - 80
                for task in milestone.tasks.filter(is_deleted=False):
                    p.setFont("Helvetica", 10)
                    p.setFillColor(colors_dict["primary_dark"])
                    p.drawString(90, task_y_position, f"• {task.title} - Status: {task.state}")
                    task_y_position -= 15

                y_position -= block_height + 30

        # Placeholder para Kanban Board
        if settings.include_kanban_board:
            y_position = draw_section_title("Kanban Board", y_position, p, colors_dict)
            p.setFont("Helvetica", 12)
            p.drawString(70, y_position, "Kanban board would be displayed here")

        p.showPage()
        p.save()
        buffer.seek(0)
        return buffer

    def send_report_email(self, user, project, pdf_buffer):
        email = EmailMessage(
            f'Test Project Report: {project.title}',
            'This is a test project report email.',
            'from@example.com',
            [user.email],
        )
        email.attach(f'{project.title}_test_report.pdf', pdf_buffer.getvalue(), 'application/pdf')
        email.send()

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
