from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import EmailMessage
from project.models import Project, ProjectReportSettings, Task, Milestone, UserProjectReportSettings
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib import colors
from reportlab.lib.units import inch
from datetime import timedelta
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from datetime import timedelta
class Command(BaseCommand):
    help = 'Generates periodic project reports based on user settings'

    def handle(self, *args, **options):
        today = timezone.now().date()
        user_report_settings = UserProjectReportSettings.objects.all()

        for user_settings in user_report_settings:
            settings = user_settings.report_settings
            if self.should_generate_report(settings, today):
                pdf_buffer = self.generate_report(settings.project, settings)
                self.send_report_email(user_settings.user, settings.project, pdf_buffer)

    def should_generate_report(self, settings, today):
        frequency = settings.report_frequency
        return (
            frequency == 'daily' or
            (frequency == 'weekly' and today.weekday() == 0) or  # Monday
            (frequency == 'monthly' and today.day == 1)
        )
    def generate_report(self, project, settings):
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        # Custom colors for improved design
        colors_dict = {
            "header": colors.HexColor("#3D46F2"),
            "section_title": colors.HexColor("#121670"),
            "task_complete": colors.HexColor("#4CAF50"),
            "task_inprogress": colors.HexColor("#FFC107"),
            "kanban_bg": colors.HexColor("#F0F1FC")
        }

        def draw_header():
            p.setFillColor(colors_dict["header"])
            p.roundRect(0, height - 60, width, 60, 10, fill=True)
            p.setFillColor(colors.white)
            p.setFont("Helvetica-Bold", 22)
            p.drawCentredString(width/2, height - 35, f"Project Report: {project.title}")

        def new_page():
            p.showPage()
            draw_header()
            return height - 120  # Start content further down on new pages

        def check_page_break(y_position, needed_space):
            if y_position - needed_space < 50:  # Leave some margin at the bottom
                return new_page()
            return y_position

        # Helper function to draw section titles
        def draw_section_title(title, y):
            y = check_page_break(y, 50)
            p.setFillColor(colors_dict["section_title"])
            p.setFont("Helvetica-Bold", 16)
            p.drawString(50, y, title)
            return y - 30

        y_position = height - 60  # Start at the top of the first page
        draw_header()
        y_position -= 30  # Move down after the header

        # Milestone Progress Section
        if settings.include_milestone_progress:
            y_position = draw_section_title("Milestone Progress", y_position)
            milestone_progress = self.calculate_milestone_progress(project)
            p.setFont("Helvetica", 12)
            p.setFillColor(colors.black)
            p.drawString(70, y_position, f"Overall progress: {milestone_progress:.2f}%")
            y_position -= 50

        # Task Progress Section
        if settings.include_task_progress:
            y_position = draw_section_title("Task Progress", y_position)
            task_progress = self.calculate_task_progress(project)
            p.setFont("Helvetica", 12)
            p.setFillColor(colors.black)
            p.drawString(70, y_position, f"Overall progress: {task_progress:.2f}%")
            y_position -= 50

        # Milestones and Tasks Section
        if settings.include_milestones_and_tasks:
            y_position = draw_section_title("Milestones and Tasks", y_position)

            for milestone in project.milestones.filter(is_deleted=False):
                num_tasks = milestone.tasks.filter(is_deleted=False).count()
                block_height = 80 + (num_tasks * 15)
                
                y_position = check_page_break(y_position, block_height + 30)

                p.setFillColor(colors_dict["kanban_bg"])
                p.roundRect(50, y_position - block_height, 500, block_height, 5, fill=True, stroke=False)

                p.setFont("Helvetica-Bold", 12)
                p.setFillColor(colors_dict["section_title"])
                p.drawString(70, y_position - 30, f"Milestone: {milestone.name}")

                p.setFont("Helvetica", 10)
                p.setFillColor(colors.black)
                p.drawString(70, y_position - 45, f"Progress: {milestone.amount_completed}/{milestone.tasks.count()} assignments completed")
                p.drawString(70, y_position - 60, f"Deadline: {milestone.end_date}")

                status_color = (
                    colors_dict["task_complete"] if milestone.amount_completed == milestone.tasks.count()
                    else colors_dict["task_inprogress"]
                )
                p.setFillColor(status_color)
                p.circle(520, y_position - 50, 5, fill=True)

                task_y_position = y_position - 80
                for task in milestone.tasks.filter(is_deleted=False):
                    p.setFont("Helvetica", 10)
                    p.setFillColor(colors_dict["section_title"])
                    p.drawString(90, task_y_position, f"• {task.title} - Status: {task.state}")
                    task_y_position -= 15

                y_position -= block_height + 30

        # Kanban Board Section
        if settings.include_kanban_board:
            y_position = draw_section_title("Kanban Board", y_position)
            p.setFont("Helvetica", 12)

            states = ['pendiente', 'En progreso', 'Completada']
            for state in states:
                y_position = check_page_break(y_position, 50)
                p.setFillColor(colors.black)
                p.drawString(70, y_position, f"Column: {state}")
                y_position -= 15

                tasks = Task.objects.filter(milestone__project=project, state=state, is_deleted=False)
                for task in tasks:
                    y_position = check_page_break(y_position, 20)
                    p.drawString(90, y_position, f"Task: {task.title}")
                    y_position -= 15

                y_position -= 10

        # Gantt Chart Section
        if settings.include_gantt_chart:
            y_position = draw_section_title("Gantt Chart", y_position)
            p.setFont("Helvetica", 12)
            y_position -= 30
            
            milestones = project.milestones.filter(is_deleted=False).order_by('start_date')
            
            if milestones.exists():
                start_date = milestones.first().start_date
                end_date = max(m.end_date for m in milestones)
                total_days = (end_date - start_date).days + 1
                
                chart_width = 5 * inch
                chart_height = 0.5 * inch * len(milestones)  # Increased height for better spacing
                left_margin = 2.5 * inch
                
                # Function to draw the time scale
                def draw_time_scale(y):
                    p.setFont("Helvetica-Bold", 8)  # Bold font for better readability
                    p.setFillColor(colors.black)  # Ensure text color is black
                    for i in range(total_days + 1):
                        x = left_margin + (i / total_days) * chart_width
                        p.line(x, y, x, y - 0.1 * inch)
                        if i % 7 == 0:  # Label every week
                            date_label = (start_date + timedelta(days=i)).strftime('%m/%d')
                            label_width = p.stringWidth(date_label, "Helvetica-Bold", 8)
                            p.drawString(x - label_width / 2, y + 5, date_label)
                    
                    # Draw horizontal line under the time scale
                    p.line(left_margin, y - 0.1 * inch, left_margin + chart_width, y - 0.1 * inch)
                
                # Draw milestones
                for i, milestone in enumerate(milestones):
                    y_position = check_page_break(y_position, 0.7 * inch)
                    
                    if i == 0 or y_position == height - 120:  # Draw time scale at the top of each page
                        draw_time_scale(y_position)
                        y_position -= 0.3 * inch
                    
                    # Draw milestone name
                    p.setFont("Helvetica", 10)
                    p.setFillColor(colors.black)
                    p.drawString(0.1 * inch, y_position, milestone.name[:30])  # Truncate long names
                    
                    # Draw milestone bar
                    milestone_start = (milestone.start_date - start_date).days
                    milestone_duration = (milestone.end_date - milestone.start_date).days + 1
                    
                    x_start = left_margin + (milestone_start / total_days) * chart_width
                    x_width = (milestone_duration / total_days) * chart_width
                    
                    p.setFillColor(colors.lightblue)
                    p.rect(x_start, y_position - 0.15 * inch, x_width, 0.3 * inch, fill=1, stroke=1)
                    
                    # Add start and end dates to the milestone bar
                    p.setFont("Helvetica", 7)
                    p.setFillColor(colors.black)
                    start_date_str = milestone.start_date.strftime('%m/%d')
                    end_date_str = milestone.end_date.strftime('%m/%d')
                    p.drawString(x_start + 2, y_position - 0.13 * inch, start_date_str)
                    p.drawString(x_start + x_width - p.stringWidth(end_date_str, "Helvetica", 7) - 2, 
                                y_position - 0.13 * inch, end_date_str)
                    
                    y_position -= 0.5 * inch  # Increased spacing between milestones
                
                # Draw final time scale if needed
                if y_position > 50:
                    draw_time_scale(y_position)
            else:
                p.drawString(120, y_position, "No milestones to display in Gantt chart")
                y_position -= 20

        p.showPage()  # Ensure the last page is saved
        p.save()
        buffer.seek(0)
        return buffer

    def send_report_email(self, user, project, pdf_buffer):
        email = EmailMessage(
            f'Project Report: {project.title}',
            'Please find attached the latest project report.',
            'from@example.com',
            [user.email],
        )
        email.attach(f'{project.title}_report.pdf', pdf_buffer.getvalue(), 'application/pdf')
        email.send()

    def calculate_milestone_progress(self, project):
        milestones = project.milestones.filter(is_deleted=False)
        total_milestones = milestones.count()
        if total_milestones == 0:
            return 0

        completed_milestones = 0
        for milestone in milestones:
            total_tasks = milestone.tasks.count()  # Usa 'tasks' como el related_name correcto
            completed_tasks = milestone.tasks.filter(state='Completada').count()

            # Si todas las tareas están completadas, el hito se considera completado
            if total_tasks > 0 and completed_tasks == total_tasks:
                completed_milestones += 1

        return (completed_milestones / total_milestones) * 100



    def calculate_task_progress(self, project):
        tasks = Task.objects.filter(milestone__project=project, is_deleted=False)
        total_tasks = tasks.count()
        completed_tasks = tasks.filter(state='Completada').count()
        return (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
