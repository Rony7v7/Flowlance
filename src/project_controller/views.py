from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = request.user
            project.save()
            return redirect("my_projects")
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
    project = Project.objects.get(id=project_id)

    sections_map = {
        "hitos": "projects/milestones.html",
        "tareas": "projects/tasks.html",
        "linea_de_tiempo": "projects/time_line.html",
        "calendario": "projects/calendar.html",
    }

    section_to_show = sections_map.get(section, "project/milestones.html")

    return render(
        request,
        section_to_show,
        {
            "project": project,
            "milestones": project.milestones.all(),
            "section":section
        },
    )
