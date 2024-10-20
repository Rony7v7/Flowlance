from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from flowlance.decorators import role_required
from project.models import Assigment, Milestone

@role_required(['administrator', 'member'])
@login_required
def create_assigment(request, milestone_id):
    milestone = get_object_or_404(Milestone,id=milestone_id,is_deleted=False)
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

@role_required(['administrator', 'member'])
@login_required
def edit_assigment(request, assigment_id):
    assigment = get_object_or_404(Assigment,id=assigment_id,is_deleted=False)
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

@role_required(['administrator', 'member'])
@login_required
def delete_assigment(request, assigment_id):
    assigment = get_object_or_404(Assigment, id=assigment_id,is_deleted=False)
    milestone_id = assigment.milestone.id

    if request.method == "POST":
        assigment.is_deleted = True
        assigment.save()
        return redirect("edit_milestone", milestone_id=milestone_id)

@role_required(['administrator', 'member'])
@login_required
def upload_assigment(request, assigment_id):
    assigment = get_object_or_404(Assigment, id=assigment_id,is_deleted=False)

    if request.method == "POST":
        if request.FILES.get("entregable"):
            assigment.file = request.FILES["entregable"]
            assigment.save()
            messages.success(request, "Archivos subido con exito!")
            return redirect("edit_milestone", milestone_id=assigment.milestone.id)

    return render(
        request, "projects/upload_assigment_file.html", {"assigment": assigment}
    )

def get_assigment_information(request, assigment_id):
    assigment = get_object_or_404(Assigment, id=assigment_id,is_deleted=False)
    return render(
        request,"projects/assigment_information.html",{"assigment": assigment}
    )