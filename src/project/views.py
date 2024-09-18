from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Milestone, Project
from django.http import Http404
from datetime import datetime
from django.db.models import Prefetch


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

    if request.method == "POST":
        # Get data from the POST request

        # Redirect to the project view
        return redirect("project", project_id=milestone.project.id, section="milestone")

    return render(
        request,
        "projects/manage_milestone.html",
        {
            "milestone": milestone,
            "is_editing": True,
            "project_id": milestone.project.id,
        },
    )
