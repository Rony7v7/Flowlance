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
            return redirect(
                "my_projects"
            )  
    else:
        form = ProjectForm()
    return render(request, "projects/create_project.html", {"form": form})


@login_required
def my_projects(request):
    projects = Project.objects.filter(client=request.user)
    return render(request, "projects/my_projects.html", {"projects": projects})

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
        }
    ]

    return render(request, "projects/project_list.html", {"projects": projects})