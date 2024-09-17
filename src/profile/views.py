from django.shortcuts import render, redirect
from .forms import PortfolioProjectForm, CurriculumVitaeForm, CourseForm
from .models import PortfolioProject, CurriculumVitae, Course

def profile(request):
    return render(request, 'navigation/building.html')

def create_project_portfolio(request):
    if request.method == 'POST':
        form = PortfolioProjectForm(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.profile = request.user  # Ajustamos el nombre a profile (user)
            proyecto.save()
            return redirect('proyecto_exito')  # Cambia a la URL que consideres para el éxito
    else:
        form = PortfolioProjectForm()
    return render(request, 'profile/create_project_portfolio.html', {'form': form})

def upload_curriculum(request):
    if request.method == 'POST':
        form = CurriculumVitaeForm(request.POST, request.FILES)
        if form.is_valid():
            curriculum = form.save(commit=False)
            curriculum.profile = request.user  # Ajustamos a profile (user)
            curriculum.save()
            return redirect('curriculum_exito')
    else:
        form = CurriculumVitaeForm()
    return render(request, 'profile/upload_curriculum.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.profile = request.user  # Ajustamos a profile (user)
            curso.save()
            return redirect('curso_exito')  
    else:
        form = CourseForm()
    return render(request, 'profile/add_course.html', {'form': form})
