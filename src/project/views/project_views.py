from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from profile.models import Notification
from project.forms import ProjectForm
from project.models import Application, Milestone, Project
from django.contrib import messages

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
    try:

        project = get_object_or_404(
            Project.objects.only("title", "description")
            .prefetch_related(
                Prefetch("milestones", queryset=Milestone.objects.order_by("end_date"))
            ),
            id=project_id,
            is_deleted=False
        )
    except Project.DoesNotExist:
        raise Http404("No Project with that id")

    milestones = project.milestones.filter(is_deleted=False)

    milestone_data = [
        {
            'id': milestone.id,
            'group': milestone.project.id,  # Group by project or another criterion
            'content': milestone.name,
            'start': milestone.start_date.strftime('%Y-%m-%d'),
            'end': milestone.end_date.strftime('%Y-%m-%d'),
        }
        for milestone in milestones
    ]

    # Get all applications for the project
    applications = project.applications.filter(is_deleted=False)

    sections_map = {
        "milestone": "projects/milestones.html",
        "task": "projects/tasks.html",
        "time_line": "projects/time_line.html",
        "calendar": "projects/calendar.html",
    }

    section_to_show = sections_map.get(section, "projects/milestones.html")
    application = project.applications.filter(user=request.user,is_deleted=False).first()

    return render(
        request,
        section_to_show,

        {
            "project": project,
            "milestones": milestones,
            "milestone_data": milestone_data,  # Pass serialized data to template
            "section": section,
            "application": application,
            "applications": applications,
        },
    )

@login_required
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


