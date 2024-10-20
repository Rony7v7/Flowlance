from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from profile.models import Notification
from project.forms import ProjectForm, ProjectUpdateForm
from project.models import Application, Milestone, Project, Task, ProjectUpdate, UpdateComment
from django.contrib import messages

@login_required
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
    projects = Project.objects.filter(client=request.user)
    return render(
        request,
        "projects/my_projects.html",
        {
            "projects": projects,
        },
    )



@login_required
def display_project(request, project_id, section):
    try:
        project = (
            Project.objects.prefetch_related(
                Prefetch("milestones", queryset=Milestone.objects.order_by("end_date").prefetch_related("tasks"))
            ).get(id=project_id)
        )
    except Project.DoesNotExist:
        raise Http404("No Project with that id")

    milestones = project.milestones.all()

    # Progreso de cada hito (calculado en la vista)
    milestone_progress_data = []
    for milestone in milestones:
        total_deliverables = milestone.assigments.count()  # Número total de entregables
        completed_deliverables = milestone.amount_completed  # Número de entregables completados
        if total_deliverables > 0:
            progress = (completed_deliverables / total_deliverables) * 100
        else:
            progress = 0
        milestone_progress_data.append({
            'milestone': milestone,
            'progress': progress,
        })

    # Progreso de Tareas
    tasks = Task.objects.filter(milestone__in=milestones)
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

    # Si la sección es "updates", obtener las actualizaciones del proyecto
    if section == "updates":
        updates = ProjectUpdate.objects.filter(project=project).order_by('-created_at')
    else:
        updates = None

    # Obtener el parámetro GET que indica si se muestran solo las importantes
    show_important = request.GET.get('show_important', 'false').lower() == 'true'

    # Filtrar actualizaciones según el parámetro
    if show_important:
        updates = ProjectUpdate.objects.filter(project=project, is_important=True)
    else:
        updates = ProjectUpdate.objects.filter(project=project)

    sections_map = {
        "milestone": "projects/milestones.html",
        "task": "projects/tasks.html",
        "time_line": "projects/time_line.html",
        "calendar": "projects/calendar.html",
        "data_project": "projects/data_project.html",
        "updates": "projects/updates.html",  # Nueva sección de actualizaciones
    }

    section_to_show = sections_map.get(section, "projects/milestones.html")

    return render(
        request,
        section_to_show,
        {
            "project": project,
            "tasks": tasks,
            "milestones": milestones,
            "milestone_progress_data": milestone_progress_data,
            "task_progress": task_progress,
            "milestone_progress": milestone_progress,
            "section": section,
            "updates": updates,
            "show_important": show_important,  # Pasar las actualizaciones al contexto si se selecciona "updates"
        },
    )



@login_required
def project_updates(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        is_important = request.POST.get('is_important') == 'on'

        if content:
            update = ProjectUpdate.objects.create(
                project=project,
                content=content,
                is_important=is_important,
                author=request.user  # Asegúrate de que el campo 'author' esté correctamente definido en tu modelo
            )
            update.save()

        return redirect('project', project_id=project.id, section='updates')

    updates = project.updates.all()

    context = {
        'project': project,
        'updates': updates,
    }
    
    return render(request, 'projects/updates.html', context)


@login_required
def add_project_update(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST)
        if form.is_valid():
            update = form.save(commit=False)
            update.project = project
            update.author = request.user
            update.save()
            return redirect('project', project_id=project.id, section='updates')
    else:
        form = ProjectUpdateForm()

    return render(request, 'projects/add_update.html', {'form': form, 'project': project})

@login_required
def add_comment(request, update_id):
    update = get_object_or_404(ProjectUpdate, id=update_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            UpdateComment.objects.create(
                update=update,
                user=request.user,
                content=content,
            )
    return redirect('project', project_id=update.project.id, section='updates')



@login_required
def project_list_availableFreelancer(request):
    search_query = request.GET.get("search", "")  # Captura el valor del input 'search'
    projects = Project.objects.all()  # Obtiene todos los proyectos inicialmente
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
def project_list(request):
    projects = Project.objects.filter(client=request.user)
    return render(request, "projects/project_list.html", {"projects": projects})



@login_required
def project_edit(request, pk):
    
    project = get_object_or_404(Project, pk=pk, client=request.user)
    
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
    
    project = get_object_or_404(Project, pk=pk, client=request.user)
    
    if request.method == "POST":
        
        project_title = project.title
        project.delete()

        
        Notification.objects.create(
            user=request.user,
            message=f"El proyecto '{project_title}' ha sido eliminado exitosamente."
        )

        
        return redirect("project_list")
    
    return render(request, "projects/project_delete.html", {"project": project})



@login_required
def project_requirements(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, "projects/project_requirements.html", {"project": project})

@login_required
def apply_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    
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
    application = get_object_or_404(Application, id=application_id)

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
        'section': 'data_project',  # Aseguramos que la pestaña "Informes" esté activa
    }
    return render(request, 'projects/data_project.html', context)





