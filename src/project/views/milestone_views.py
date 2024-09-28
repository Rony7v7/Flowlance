from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from project.models import Milestone, Project

@login_required
def add_milestone(request, project_id):
    # Retrieve the project or raise a 404 error if not found
    project = get_object_or_404(Project, id=project_id,is_deleted=False)

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

@login_required
def edit_milestone(request, milestone_id):
    milestone = get_object_or_404(Milestone, id=milestone_id,is_deleted=False)
    project_id = milestone.project.id
    assigments = milestone.assigments.filter(is_deleted=False)
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
            "assigments":assigments,
        },
    )


@login_required
def delete_milestone(request, milestone_id):
    milestone = get_object_or_404(Milestone, id=milestone_id,is_deleted=False)
    project_id = milestone.project.id
    if request.method == "POST":
        milestone.is_deleted = True
        milestone.save()
        return redirect("project", project_id=project_id, section="milestone")