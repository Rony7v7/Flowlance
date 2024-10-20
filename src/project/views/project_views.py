from django.http import Http404, HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from profile.models import Notification
from project.forms import ProjectForm, EventForm
from project.models import Application, Milestone, Project, Task, ProjectReportSettings
from django.contrib import messages
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from project.forms import ProjectReportSettingsForm
from project.models import  UserProjectReportSettings

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from io import BytesIO
from project.models import Project, ProjectReportSettings
from project.management.commands.generate_periodic_reports import Command as ReportCommand
# Decorators
from flowlance.decorators import client_required, freelancer_required, attach_profile_info

@login_required
@client_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = request.user
            project.save()
            project.members.add(request.user)
            id = project.id
            return redirect("project", project_id=id, section="milestone")
    else:
        form = ProjectForm()
    return render(request, "projects/create_project.html", {"form": form})


@login_required
def my_projects(request):
    projects = Project.objects.filter(client=request.user,is_deleted=False)
    return render(
        request,
        "projects/my_projects.html",
        {
            "projects": projects,
        },
    )

@login_required
@attach_profile_info
def display_project(request, project_id, section):
    project = get_object_or_404(Project, id=project_id, is_deleted=False)
    
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.project = project
            event.save()
            return JsonResponse({'status': 'success'}, status=200)  
        else:
            return JsonResponse({'errors': form.errors}, status=400) 

    milestones = project.milestones.filter(is_deleted=False)
    tasks = Task.objects.filter(milestone__in=milestones)

    task_progress, milestone_progress = getProjectProgress(milestones, tasks)

    events = project.events.all()
    event_list = [
        {
            'title': event.name,
            'id': event.id,
            'start': event.start.strftime("%Y-%m-%dT%H:%M:%S"),
            'end': event.end.strftime("%Y-%m-%dT%H:%M:%S"),
            'description': event.description,
        }
        for event in events
    ]

    sections_map = {
        "milestone": "projects/milestones.html",
        "task": "projects/tasks.html",
        "time_line": "projects/time_line.html",
        "calendar": "projects/calendar.html",
        "data_project": "projects/data_project.html",
        "deliverable" : "projects/deliverables.html"
    }

    section_to_show = sections_map.get(section, "projects/milestones.html")
    application = project.applications.filter(user=request.user, is_deleted=False).first()

    return render(
        request,
        section_to_show,
        {
            "project": project,
            "tasks": tasks,
            "milestones": milestones,
            "task_progress": task_progress,
            "milestone_progress": milestone_progress,
            "section": section,
            "application": application,
            "user_is_owner": request.user == project.client,
            "events": event_list,
            "form": EventForm(),  
        },
    )


def getProjectProgress(milestones, tasks):

    # Progreso de Tareas
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(state="Completada").count()
    task_progress = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    # Progreso de Hitos
    total_milestones = milestones.count()
    completed_milestones = 0
    for milestone in milestones:
        if milestone.amount_completed == milestone.assigments.count():
            completed_milestones += 1

    milestone_progress = (completed_milestones / total_milestones) * 100 if total_milestones > 0 else 0

    return task_progress, milestone_progress


@login_required
@attach_profile_info
def project_list_availableFreelancer(request):
    search_query = request.GET.get("search", "")  # Captura el valor del input 'search'
    projects = Project.objects.filter(is_deleted = False)  # Obtiene todos los proyectos inicialmente
    # Aqui se deben aplicar todos los filtros que se manden desde el front
    if search_query:
        projects = projects.filter(
            title=search_query
        )  # Filtra por el nombre del proyecto (title)

    return render(
        request,
        "projects/project_main_view.html",
        {"projects": projects},
    )

@login_required
@attach_profile_info
def project_list(request):
    projects = Project.objects.filter(client=request.user,is_deleted=False)
    return render(request, "projects/project_list.html", {"projects": projects})



@login_required
def project_edit(request, pk):
    
    project = get_object_or_404(Project, pk=pk, client=request.user,is_deleted=False)
    
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()

            
            Notification.objects.create(
                user=request.user,
                message=f"El proyecto '{project.title}' ha sido editado exitosamente."
            )

        return redirect("project", project_id=project.pk, section="milestone")

    else:
        form = ProjectForm(instance=project)

    return render(
        request,
        "projects/project_form.html",
        {"form": form, "project": project, "action": "Edit"},
    )


@login_required
def project_delete(request, pk):
    
    project = get_object_or_404(Project, pk=pk, client=request.user,is_deleted=False)
    
    if request.method == "POST":
        
        project_title = project.title
        project.is_deleted = True
        project.save()

        
        Notification.objects.create(
            user=request.user,
            message=f"El proyecto '{project_title}' ha sido eliminado exitosamente."
        )

        
        return redirect("project_list")
    
    return render(request, "projects/project_delete.html", {"project": project})



@login_required
def project_requirements(request, project_id):
    project = get_object_or_404(Project,pk=project_id,is_deleted=False)
    return render(request, "projects/project_requirements.html", {"project": project})

@login_required
@freelancer_required
def apply_project(request, project_id):
    project = get_object_or_404(Project, id=project_id,is_deleted=False)

    
    application, created = Application.objects.get_or_create(
        user=request.user, project=project
    )

    if created:
        
        Notification.objects.create(
            user=request.user,
            message=f"Te has postulado al proyecto '{project.title}'. Tu postulación está pendiente de revisión."
        )

        
        Notification.objects.create(
            user=project.client,
            message=f"{request.user.username} se ha postulado a tu proyecto '{project.title}'."
        )

    else:
       
        Notification.objects.create(
            user=request.user,
            message=f"Ya te has postulado anteriormente al proyecto '{project.title}'."
        )

   
    return redirect("project", project_id=project_id, section="milestone")



@login_required
def update_application_status(request, application_id, action):
    application = get_object_or_404(Application, id=application_id,is_deleted=False)

    if request.user != application.project.client:
        return HttpResponseForbidden(
            "No tienes permiso para modificar esta postulación."
        )

    if action == "accept":
        application.status = "Aceptada"
        message = f"Tu postulación al proyecto '{application.project.title}' ha sido aceptada."
        application.project.members.add(application.user)
    elif action == "reject":
        application.status = "Rechazada"
        message = f"Tu postulación al proyecto '{application.project.title}' ha sido rechazada."
    else:
        messages.error(request, "Acción inválida.")
        return redirect(
            "project", project_id=application.project.id, section="milestone"
        )

    application.save()

    Notification.objects.create(user=application.user, message=message)

    messages.success(request, f"La postulación ha sido {application.status.lower()}.")
    return redirect("project", project_id=application.project.id, section="milestone")

@login_required
def data_project_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project': project,
        'section': 'data_project',  
    }
    return render(request, 'projects/data_project.html', context)


@login_required
def report_settings(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    user_settings, created = UserProjectReportSettings.objects.get_or_create(
        user=request.user,
        report_settings__project=project,
        defaults={'report_settings': ProjectReportSettings.objects.create(project=project)}
    )
    settings = user_settings.report_settings

    if request.method == 'POST':
        form = ProjectReportSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            return redirect(reverse('project', kwargs={'project_id': project.id, 'section': 'data_project'})) 
    else:
        form = ProjectReportSettingsForm(instance=settings)

    return render(request, 'projects/report_settings.html', {'form': form, 'project': project})

login_required
def generate_project_report(request, project_id):
    project = get_object_or_404(Project, id=project_id, is_deleted=False)
    settings, _ = ProjectReportSettings.objects.get_or_create(project=project)

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    p.drawString(100, 750, f"Project Report: {project.title}")
    
    y_position = 700
    
    if settings.include_milestone_progress:
        p.drawString(100, y_position, "Milestone Progress")
        y_position -= 20
        milestone_progress = calculate_milestone_progress(project)
        p.drawString(120, y_position, f"Overall progress: {milestone_progress}%")
        y_position -= 40
    
    if settings.include_task_progress:
        p.drawString(100, y_position, "Task Progress")
        y_position -= 20
        task_progress = calculate_task_progress(project)
        p.drawString(120, y_position, f"Overall progress: {task_progress}%")
        y_position -= 40
    
    if settings.include_milestones_and_tasks:
        p.drawString(100, y_position, "Milestones and Tasks")
        y_position -= 20
        for milestone in project.milestones.filter(is_deleted=False):
            p.drawString(120, y_position, f"Milestone: {milestone.name}")
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
            tasks = project.tasks.filter(state=state, is_deleted=False)
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
    return FileResponse(buffer, as_attachment=True, filename=f'{project.title}_report.pdf')

def calculate_milestone_progress(project):
    milestones = project.milestones.filter(is_deleted=False)
    total_milestones = milestones.count()
    if total_milestones == 0:
        return 0

    completed_milestones = sum(
        1 for milestone in milestones
        if milestone.amount_completed == milestone.assigments.count() and milestone.assigments.count() > 0
    )

    return (completed_milestones / total_milestones) * 100

def calculate_task_progress(project):
    tasks = Task.objects.filter(milestone__project=project, is_deleted=False)
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(state='Completada').count()
    return (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

@login_required
def download_project_report(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    # Get all settings for the project
    settings_queryset = ProjectReportSettings.objects.filter(project=project)
    
    if not settings_queryset.exists():
        raise Http404("No report settings found for this project.")
    
    # Use the first settings object (you might want to add logic to choose the most appropriate one)
    settings = settings_queryset.first()
    
    # Use the existing report generation logic
    report_command = ReportCommand()
    pdf_buffer = report_command.generate_report(project, settings)
    
    # Create the HTTP response with PDF mime type
    response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{project.title}_report.pdf"'
    
    return response