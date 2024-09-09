from django.shortcuts import render, redirect
from .forms import PortfolioProjectForm, CurriculumVitaeForm, CursoForm
from .models import PortfolioProject, CurriculumVitae, Curso

def crear_proyecto_portafolio(request):
    if request.method == 'POST':
        form = PortfolioProjectForm(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.perfil = request.user
            proyecto.save()
            return redirect('proyecto_exito')  
    else:
        form = PortfolioProjectForm()
    return render(request, 'freelancer_profile_creation/crear_proyecto_portafolio.html', {'form': form})

def subir_curriculum(request):
    if request.method == 'POST':
        form = CurriculumVitaeForm(request.POST, request.FILES)
        if form.is_valid():
            curriculum = form.save(commit=False)
            curriculum.perfil = request.user
            curriculum.save()
            return redirect('curriculum_exito')
    else:
        form = CurriculumVitaeForm()
    return render(request, 'freelancer_profile_creation/subir_curriculum.html', {'form': form})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.perfil = request.user
            curso.save()
            return redirect('curso_exito')  
    else:
        form = CursoForm()
    return render(request, 'freelancer_profile_creation/agregar_curso.html', {'form': form})
