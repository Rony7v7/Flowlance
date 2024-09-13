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
    if section == "hitos":
        return render(
            request,
            "projects/project.html",
            {
                "project": project,
                "milestones": project.milestones.all(),
                "section": section,
            },
        )

    return render(
        request,
        "projects/",
        {"project": project, "milestones": project.milestones.all()},
    )
