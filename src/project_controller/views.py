from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project
from django.http import Http404


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
    try:
        project = Project.objects.only("title","description").get(id=project_id)
    except Project.DoesNotExist:
        raise Http404("No Project with that id")

    sections_map = {
        "milestone": "projects/milestones.html",
        "task": "projects/tasks.html",
        "time_line": "projects/time_line.html",
        "calendar": "projects/calendar.html",
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
