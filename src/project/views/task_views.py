from datetime import datetime
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from project.models import Comment, Milestone, Project, Task, TaskDescription, TaskFile
from profile.models import Notification
from django.contrib.auth.models import User

@login_required
def create_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    milestones = project.milestones.all()

    print(project.members.all())
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        end_date_str = request.POST.get("end_date")
        priority = request.POST.get("priority")
        state = request.POST.get("state")
        user_id = request.POST.get("user")
        milestone_id = request.POST.get("milestone")
        milestone = Milestone.objects.get(id=milestone_id)
        user = get_object_or_404(User, id=user_id)
        allowed_prioritied = ["baja", "media", "alta"]
        allowed_states = ["pendiente", "En progreso", "Completada"]
        if (
            milestone == None
            or priority not in allowed_prioritied
            or state not in allowed_states
        ):
            return render(
                request,
                "projects/task_creation.html",
                {
                    "project_id": project_id,
                    "milestones": milestones,
                    "members": project.members.all(),
                },
            )

        if name == "" or description == "" or user not in project.members.all():
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
            responsible=user,
        )

        messages.success(request, "task created")
        return redirect("project", project_id=project_id, section="task")
    return render(
        request,
        "projects/task_creation.html",
        {
            "project_id": project_id,
            "milestones": milestones,
            "members": project.members.all(),
        },
    )

@login_required
def edit_description(request, description_id):

    description = get_object_or_404(TaskDescription, id=description_id)
    project_id = description.task.milestone.project.id

    if request.user != description.user and not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permiso para editar esta descripción.")

    if request.method == "POST":
        content = request.POST.get("content")
        if content:

            description.content = content
            description.save()

            return redirect("project", project_id=project_id, section="task")

    # Renderizar la plantilla desde la ubicación correcta
    return render(
        request, "projects/edit_description.html", {"description": description}
    )


@login_required
def add_description(request, task_id):

    task = get_object_or_404(Task, id=task_id)
    project_id = task.milestone.project.id

    if request.method == "POST":
        content = request.POST.get("content")
        if content:

            TaskDescription.objects.create(
                task=task, user=request.user, content=content
            )

        return redirect("project", project_id=project_id, section="task")

    return render(
        request, "tasks/manage_task.html", {"task_id": task_id, "is_editing": False}
    )

@login_required
def add_comment(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project_id = task.milestone.project.id

    if request.method == "POST":
        content = request.POST.get("content")
        if content:

            Comment.objects.create(task=task, user=request.user, content=content)

            Notification.objects.create(
                user=request.user,
                message=f"Has añadido un comentario a la tarea '{task.title}' en el proyecto '{task.milestone.project.title}'."
            )

            if task.responsible and task.responsible != request.user:
                Notification.objects.create(
                    user=task.responsible,
                    message=f"{request.user.username} ha añadido un comentario a la tarea '{task.title}' en el proyecto '{task.milestone.project.title}'."
                )

        return redirect("project", project_id=project_id, section="task")

    return render(request, "tasks/manage_task.html", {"task_id": task_id, "is_editing": False})




@login_required
def add_file(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project_id = task.milestone.project.id

    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]

        TaskFile.objects.create(
            task=task,
            file=file,
        )

        Notification.objects.create(
            user=request.user,
            message=f"Has subido un archivo a la tarea '{task.title}' en el proyecto '{task.milestone.project.title}'."
        )

        if task.responsible and task.responsible != request.user:
            Notification.objects.create(
                user=task.responsible,
                message=f"{request.user.username} ha subido un archivo a la tarea '{task.title}' en el proyecto '{task.milestone.project.title}'."
            )

        
        return redirect("project", project_id=project_id, section="task")

    return render(request, "tasks/manage_task.html", {"task_id": task_id, "is_editing": False})


@login_required
def update_task_state(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    # Verifica que el usuario tenga permisos para editar el estado de la tarea
    if request.user != task.responsible and not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permisos para actualizar esta tarea.")

    if request.method == 'POST':
        new_state = request.POST.get('state')
        task.state = new_state
        task.save()

        # Crear la notificación para el responsable de la tarea
        Notification.objects.create(
            user=task.responsible,
            message=f"{request.user.username} ha cambiado el estado de la tarea '{task.title}' a '{new_state}' en el proyecto '{task.milestone.project.title}'."
        )

        return redirect('project', project_id=task.milestone.project.id, section='task')

    return redirect('project', project_id=task.milestone.project.id, section='task')