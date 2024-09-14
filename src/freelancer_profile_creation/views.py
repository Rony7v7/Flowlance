from django.shortcuts import render, redirect
from .forms import PortfolioProjectForm, CurriculumVitaeForm, CourseForm
from .models import PortfolioProject, CurriculumVitae, Course

def create_project_portfolio(request):
    if request.method == 'POST':
        form = PortfolioProjectForm(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.perfil = request.user
            proyecto.save()
            return redirect('proyecto_exito')  
    else:
        form = PortfolioProjectForm()
    return render(request, 'freelancer_profile_creation/create_project_portfolio.html', {'form': form})

def upload_curriculum(request):
    if request.method == 'POST':
        form = CurriculumVitaeForm(request.POST, request.FILES)
        if form.is_valid():
            curriculum = form.save(commit=False)
            curriculum.perfil = request.user
            curriculum.save()
            return redirect('curriculum_exito')
    else:
        form = CurriculumVitaeForm()
    return render(request, 'freelancer_profile_creation/upload_curriculum.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.perfil = request.user
            curso.save()
            return redirect('curso_exito')  
    else:
        form = CourseForm()
    return render(request, 'freelancer_profile_creation/add_course.html', {'form': form})


