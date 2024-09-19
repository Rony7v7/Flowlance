from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Milestone, Project, Task, Comment, TaskDescription, TaskFile
from django.http import Http404
from datetime import datetime
from django.db.models import Prefetch
from django.http import HttpResponseForbidden


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = request.user
            project.save()
            id = project.id
            return redirect("project", project_id=id, section="milestone")
    else:
        form = ProjectForm()
    return render(request, "projects/create_project.html", {"form": form})


@login_required
def list_projects(request):
    # projects = Project.objects.all()

    # Proyectos de prueba

    projects = [
        {
            "title": "Proyecto 1",
            "description": "Descripción del proyecto 1",
            "budget": 1000,
            "deadline": "2021-12-31",
        },
        {
            "title": "Proyecto 2",
            "description": "Descripción del proyecto 2",
            "budget": 2000,
            "deadline": "2021-12-31",
        },
        {
            "title": "Proyecto 3",
            "description": "Descripción del proyecto 3",
            "budget": 3000,
            "deadline": "2021-12-31",
        },
    ]

    return render(request, "projects/project_list.html", {"projects": projects})


@login_required
def display_project(request, project_id, section):
    try:
        # Use `prefetch_related` to reduce the number of queries
        project = (
            Project.objects.only("title", "description")
            .prefetch_related(
                Prefetch("milestones", queryset=Milestone.objects.order_by("end_date"))
            )
            .get(id=project_id)
        )
    except Project.DoesNotExist:
        raise Http404("No Project with that id")

    sections_map = {
        "milestone": "projects/milestones.html",
        "task": "projects/tasks.html",
        "time_line": "projects/time_line.html",
        "calendar": "projects/calendar.html",
    }

    section_to_show = sections_map.get(section, "projects/milestones.html")

    return render(
        request,
        section_to_show,
        {
            "project": project,
            "milestones": project.milestones.all(),  # Already ordered by end_date
            "section": section,
        },
    )


@login_required
def add_milestone(request, project_id):
    # Retrieve the project or raise a 404 error if not found
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        # Get data from the POST request
        name = request.POST.get("name")
        description = request.POST.get("description")
        end_date_str = request.POST.get("end_date")

        if name == "" or description == "":
            return redirect("project", project_id=project_id, section="milestone")

        # Validate and parse end_date
        try:
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            return redirect("project", project_id=project_id, section="milestone")

        # Create and save the new milestone
        Milestone.objects.create(
            name=name,
            description=description,
            end_date=end_date,
            project=project,
        )

        # Redirect to the project view
        return redirect("project", project_id=project_id, section="milestone")

    return render(
        request,
        "projects/manage_milestone.html",
        {"project_id": project_id, "is_editing": False},
    )


def edit_milestone(request, milestone_id):
    milestone = get_object_or_404(Milestone, id=milestone_id)
    project_id = milestone.project.id

    if request.method == "POST":
        # Get data from the POST request
        name = request.POST.get("name")
        description = request.POST.get("description")
        end_date_str = request.POST.get("end_date")
        start_date_str = request.POST.get("start_date")

        if name == "" or description == "":
            return redirect("project", project_id=project_id, section="milestone")

        # Validate and parse end_date
        try:
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            return redirect("project", project_id=project_id, section="milestone")

        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            return redirect("project", project_id=project_id, section="milestone")

        milestone.name = name
        milestone.description = description
        milestone.end_date = end_date
        milestone.start_date = start_date
        # Save changes to the database
        milestone.save()
        # Redirect to the project view
        return redirect("project", project_id=project_id, section="milestone")

    return render(
        request,
        "projects/manage_milestone.html",
        {
            "milestone": milestone,
            "is_editing": True,
            "project_id": project_id,
        },
    )


def delete_milestone(request, milestone_id):
    milestone = get_object_or_404(Milestone, id=milestone_id)
    project_id = milestone.project.id
    if request.method == "POST":
        milestone.delete()
        return redirect("project", project_id=project_id, section="milestone")


def create_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    milestones = project.milestones.all()
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        end_date_str = request.POST.get("end_date")
        priority = request.POST.get("priority")
        state = request.POST.get("state")
        milestone_id = request.POST.get("milestone")
        milestone = Milestone.objects.get(id=milestone_id)
        if milestone == None:
            return render(
                request,
                "projects/task_creation.html",
                {"project_id": project_id, "milestones": milestones},
            )

        if name == "" or description == "":
            return redirect("project", project_id=project_id, section="task")

        # Validate and parse end_date
        try:
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            return redirect("project", project_id=project_id, section="milestone")

        Task.objects.create(
            title=name,
            description=description,
            end_date=end_date,
            priority=priority,
            state=state,
            milestone=milestone,
        )


        return redirect("project", project_id=project_id, section="task")
    return render(
        request,
        "projects/task_creation.html",
        {"project_id": project_id, "milestones": milestones},
    )


@login_required
def edit_description(request, description_id):
    # Obtener la descripción y el proyecto relacionado a través de la tarea
    description = get_object_or_404(TaskDescription, id=description_id)
    project_id = description.task.milestone.project.id  # Obtener el ID del proyecto desde la tarea relacionada

    # Verificar que el usuario es el autor de la descripción o es superusuario
    if request.user != description.user and not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permiso para editar esta descripción.")

    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            # Actualizar el contenido de la descripción
            description.content = content
            description.save()
            # Redirigir a la vista del proyecto con el project_id correcto
            return redirect("project", project_id=project_id, section="task")

    # Renderizar la plantilla desde la ubicación correcta
    return render(request, 'projects/edit_description.html', {'description': description})



@login_required
def add_description(request, task_id):
    # Obtener la tarea y el proyecto relacionado
    task = get_object_or_404(Task, id=task_id)
    project_id = task.milestone.project.id  # Obtener el ID del proyecto desde la tarea

    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            # Crear la descripción
            TaskDescription.objects.create(
                task=task,
                user=request.user,
                content=content
            )
        # Redirigir a la vista de tareas del proyecto
        return redirect("project", project_id=project_id, section="task")

    return render(request, "tasks/manage_task.html", {"task_id": task_id, "is_editing": False})


@login_required
def add_file(request, task_id):
    # Obtener la tarea y el proyecto relacionado
    task = get_object_or_404(Task, id=task_id)
    project_id = task.milestone.project.id  # Obtener el ID del proyecto desde la tarea

    if request.method == "POST" and request.FILES.get('file'):
        file = request.FILES['file']
        # Crear el archivo relacionado con la tarea
        TaskFile.objects.create(
            task=task,
            file=file,
        )
        # Redirigir a la vista de tareas del proyecto
        return redirect("project", project_id=project_id, section="task")

    return render(request, "tasks/manage_task.html", {"task_id": task_id, "is_editing": False})



@login_required
def add_comment(request, task_id):
    # Obtener la tarea y el proyecto relacionado
    task = get_object_or_404(Task, id=task_id)
    project_id = task.milestone.project.id  # Obtener el ID del proyecto desde la tarea

    if request.method == "POST":
        # Obtener el contenido del comentario desde la solicitud
        content = request.POST.get('content')
        if content:
            # Crear y guardar el comentario
            Comment.objects.create(
                task=task,
                user=request.user,
                content=content
            )
            # Redirigir a la vista de tareas del proyecto
            return redirect("project", project_id=project_id, section="task")
        else:
            # Manejar el caso en que el contenido esté vacío
            return redirect("project", project_id=project_id, section="task")

    # Renderizar la página de manejo de tareas si no es una solicitud POST
    return render(request, "tasks/manage_task.html", {"task_id": task_id, "is_editing": False})