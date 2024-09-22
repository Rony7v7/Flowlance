from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from project.models import Assigment, Milestone

@login_required
def create_assigment(request, milestone_id):
    milestone = Milestone.objects.get(id=milestone_id)
    print(milestone.project.members.all())
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        end_date_str = request.POST.get("end_date")
        user_id = request.POST.get("user")
        user = get_object_or_404(User,id=user_id)

        if user not in milestone.project.members.all():
            return redirect("create_assigment", project_id=milestone_id)

        # Validate and parse end_date
        try:
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            return redirect("create_assigment", project_id=milestone_id)
        Assigment.objects.create(
            title=name,
            creator=request.user,
            responsible= user,  
            description=description,
            milestone=milestone,
            end_date=end_date,
        )

        return redirect("edit_milestone", milestone_id=milestone_id)

    return render(
        request,
        "projects/create_assigment.html",
        {"milestone": milestone, "is_editing": False,"members":milestone.project.members.all()},
    )


def edit_assigment(request, assigment_id):
    assigment = Assigment.objects.get(id=assigment_id)
    milestone_id = assigment.milestone.id
    

    if request.method == "POST":
        # Get data from the POST request
        name = request.POST.get("name")
        description = request.POST.get("description")
        end_date_str = request.POST.get("end_date")
        user_id = request.POST.get("user")
        user = get_object_or_404(User, id = user_id)
        if name == "" or description == "" or user not in assigment.milestone.project.members.all():
            return redirect("create_assigment", milestone_id=milestone_id)

        # Validate and parse end_date
        try:
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            return redirect("create_assigment", milestone_id=milestone_id)

        assigment.title = name
        assigment.description = description
        assigment.end_date = end_date
        assigment.responsible = user

        # Save changes to the database
        assigment.save()
        # Redirect to the project view
        return redirect("edit_milestone", milestone_id=milestone_id)
    return render(
        request,
        "projects/create_assigment.html",
        {"assigment": assigment, "is_editing": True,"members":assigment.milestone.project.members.all()},
    )


def delete_assigment(request, assigment_id):
    assigment = get_object_or_404(Assigment, id=assigment_id)
    milestone_id = assigment.milestone.id

    if request.method == "POST":
        assigment.delete()
        return redirect("edit_milestone", milestone_id=milestone_id)


def upload_assigment(request, assigment_id):
    assigment = get_object_or_404(Assigment, id=assigment_id)

    if request.method == "POST":
        if request.FILES.get("entregable"):
            assigment.file = request.FILES["entregable"]
            assigment.save()
            messages.success(request, "Archivos subido con exito!")
            return redirect("edit_milestone", milestone_id=assigment.milestone.id)

    return render(
        request, "projects/upload_assigment_file.html", {"assigment": assigment}
    )