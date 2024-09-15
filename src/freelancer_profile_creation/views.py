from django.shortcuts import render, redirect
from .forms import PortfolioProjectForm, CurriculumVitaeForm, CourseForm
from django.contrib.auth.decorators import login_required
from .forms import PortfolioProjectForm, CurriculumVitaeForm, CourseForm
from .models import PortfolioProject, CurriculumVitae, Course
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

#TODO: Change proyecto -> project
@login_required
def create_project_portfolio(request):
    if request.method == 'POST':
        form = PortfolioProjectForm(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.profile = request.user  # Asociate the project with the user
            proyecto.save()
            return redirect('upload_curriculum')  
    else:
        form = PortfolioProjectForm()
    return render(request, 'freelancer_profile_creation/create_project_portfolio.html', {'form': form})



@login_required
def upload_curriculum(request):
    # Verify if the user already has a CV
    try:
        curriculum = CurriculumVitae.objects.get(profile=request.user)
    except CurriculumVitae.DoesNotExist:
        curriculum = None

    if request.method == 'POST':
        form = CurriculumVitaeForm(request.POST, request.FILES, instance=curriculum)
        if form.is_valid():
            # If the user already has a CV, update it. Otherwise, create a new one
            curriculum = form.save(commit=False)
            curriculum.profile = request.user  
            curriculum.save()
            return redirect('add_course') 
    else:
        form = CurriculumVitaeForm(instance=curriculum)  # Prepopulate the form with the user's CV
    
    return render(request, 'freelancer_profile_creation/upload_curriculum.html', {'form': form})

# Vista para agregar cursos (último paso)
@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.profile = request.user  
            curso.save()
            return redirect('freelancer_profile', username=request.user.username)  
    else:
        form = CourseForm()
    return render(request, 'freelancer_profile_creation/add_course.html', {'form': form})


@login_required
def freelancer_profile(request, username):
    # Obtener el usuario freelancer a través del nombre de usuario
    freelancer = get_object_or_404(User, username=username)
    
    # Obtener proyectos, CV y cursos asociados al freelancer
    portfolio_projects = freelancer.portfolio_projects.all()
    curriculum = freelancer.curriculumvitae if hasattr(freelancer, 'curriculumvitae') else None
    courses = freelancer.courses.all()

    context = {
        'freelancer': freelancer,
        'portfolio_projects': portfolio_projects,
        'curriculum': curriculum,
        'courses': courses
    }
    
    return render(request, 'freelancer_profile_creation/freelancer_profile.html', context)
