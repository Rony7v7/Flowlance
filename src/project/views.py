from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Assigment, Milestone, Project
from django.http import Http404
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Milestone
from .forms import ProjectForm
from .models import Milestone, Project, Task
from django.http import Http404
from datetime import datetime
from django.db.models import Prefetch
from django.contrib import messages


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
def list_projects_Rony(request):
    # projects = Project.objects.all()
    # Proyectos de prueba

    projects_available = [
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

    return render(
        request,
        "projects/project_list.html",
        {"projects_available": projects_available},
    )


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


@login_required
def project_list_availableFreelancer(request):
    search_query = request.GET.get('search', '')  # Captura el valor del input 'search'
    projects = Project.objects.all()  # Obtiene todos los proyectos inicialmente
    # Aqui se deben aplicar todos los filtros que se manden desde el front
    if search_query:
        projects = projects.filter(title =search_query)  # Filtra por el nombre del proyecto (title)
  
    return render(
        request,
        "projects/project_main_view.html",
        {"projects": projects},
    )


@login_required
def project_list(request):
    projects = Project.objects.filter(client=request.user)
    return render(request, "projects/project_list.html", {"projects": projects})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, client=request.user)
    milestones = project.milestones.all().order_by("start_date")
    return render(
        request,
        "projects/project_detail.html",
        {"project": project, "milestones": milestones},
    )


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk, client=request.user)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project_detail", pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(
        request,
        "projects/project_form.html",
        {"form": form, "project": project, "action": "Edit"},
    )


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, client=request.user)
    if request.method == "POST":
        project.delete()
        return redirect("project_list")
    return render(request, "projects/project_delete.html", {"project": project})


@login_required
def project_requirements(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, "projects/project_requirements.html", {"project": project})


@login_required
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


@login_required
def delete_milestone(request, milestone_id):
    milestone = get_object_or_404(Milestone, id=milestone_id)
    project_id = milestone.project.id
    if request.method == "POST":
        milestone.delete()
        return redirect("project", project_id=project_id, section="milestone")


@login_required
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

        messages.success(request, "task created")
        return redirect("project", project_id=project_id, section="task")
    return render(
        request,
        "projects/task_creation.html",
        {"project_id": project_id, "milestones": milestones},
    )


@login_required
def create_assigment(request, milestone_id):
    milestone = Milestone.objects.get(id=milestone_id)

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        end_date_str = request.POST.get("end_date")

        # Validate and parse end_date
        try:
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            return redirect("create_assigment", project_id=milestone_id)
        Assigment.objects.create(
            title=name,
            creator=request.user,
            responsible=None,  # TODO: ADD THE RESPONSIBLE OF THE TASK
            description=description,
            milestone=milestone,
            end_date=end_date,
        )

        return redirect("edit_milestone", milestone_id=milestone_id)

    return render(
        request,
        "projects/create_assigment.html",
        {"milestone": milestone, "is_editing": False},
    )


def edit_assigment(request, assigment_id):
    assigment = Assigment.objects.get(id=assigment_id)
    milestone_id = assigment.milestone.id

    if request.method == "POST":
        # Get data from the POST request
        name = request.POST.get("name")
        description = request.POST.get("description")
        end_date_str = request.POST.get("end_date")

        if name == "" or description == "":
            return redirect("create_assigment", milestone_id=milestone_id)

        # Validate and parse end_date
        try:
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            return redirect("create_assigment", milestone_id=milestone_id)

        assigment.title = name
        assigment.description = description
        assigment.end_date = end_date

        # Save changes to the database
        assigment.save()
        # Redirect to the project view
        return redirect("edit_milestone", milestone_id=milestone_id)
    return render(
        request,
        "projects/create_assigment.html",
        {"assigment": assigment, "is_editing": True},
    )


def delete_assigment(request, assigment_id):
    assigment = get_object_or_404(Assigment, id=assigment_id)
    milestone_id = assigment.milestone.id

    if request.method == "POST":
        assigment.delete()
        return redirect("edit_milestone", milestone_id=milestone_id)

def upload_assigment(request, assigment_id):
    assigment = get_object_or_404(Assigment, id=assigment_id)
        
    if request.method == 'POST':
            if request.FILES.get('entregable'):
                assigment.file = request.FILES['entregable']
                assigment.save()
                messages.success(request,"File uploaded correctly!")
                return redirect('edit_milestone', milestone_id=assigment.milestone.id)
        
    return render(request, 'projects/upload_assigment_file.html', {'assigment': assigment})