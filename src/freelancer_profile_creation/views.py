from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import FreelancerProfile

from .forms import (
    PortfolioProjectForm, 
    CurriculumVitaeForm, 
    CourseForm, 
    FreelancerSkillsForm, 
    WorkExperienceForm
)
from .models import (
    PortfolioProject, 
    CurriculumVitae, 
    Course, 
    Skill, 
    WorkExperience
)


@login_required
def add_skills(request):
    if request.method == 'POST':
        form = FreelancerSkillsForm(request.POST)
        if form.is_valid():
            # Save predefined skills
            selected_skills = form.cleaned_data['skills']
            for skill in selected_skills:
                request.user.freelancerprofile.skills.add(skill)

            # Save custom skills
            custom_skills = form.cleaned_data['custom_skills']
            if custom_skills:
                custom_skills_list = [skill.strip() for skill in custom_skills.split(',')]
                for custom_skill in custom_skills_list:
                    skill_obj, created = Skill.objects.get_or_create(name=custom_skill, is_custom=True)
                    request.user.freelancerprofile.skills.add(skill_obj)

            return redirect('add_experience')  
    else:
        form = FreelancerSkillsForm()

    return render(request, 'freelancer_profile_creation/add_skills.html', {'form': form})


@login_required
def add_experience(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.freelancer = request.user
            experience.save()
            return redirect('freelancer_profile', username=request.user.username) 
    else:
        form = WorkExperienceForm()

    return render(request, 'freelancer_profile_creation/add_experience.html', {'form': form})


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
def freelancer_own_profile(request):
    # Si es un superusuario, redirigir al panel de administración
    if request.user.is_superuser:
        return redirect('/admin/')
    
    try:
        # Intentar obtener el perfil del freelancer
        profile = request.user.freelancerprofile
    except FreelancerProfile.DoesNotExist:
        # Si no existe el perfil, redirigir a la página de advertencia
        return redirect('no_freelancer_profile')

    # Obtener información relacionada con el freelancer
    skills = profile.skills.all()
    work_experiences = profile.user.work_experiences.all()
    portfolio_projects = PortfolioProject.objects.filter(profile=request.user)
    curriculum = CurriculumVitae.objects.filter(profile=request.user).first()
    courses = Course.objects.filter(profile=request.user)

    context = {
        'profile': profile,
        'skills': skills,
        'work_experiences': work_experiences,
        'portfolio_projects': portfolio_projects,
        'curriculum': curriculum,
        'courses': courses,
    }
    
    return render(request, 'freelancer_profile_creation/freelancer_profile.html', context)


@login_required
def freelancer_profile(request, username):
    # Verificar si el perfil del freelancer con el username existe
    profile_exists = FreelancerProfile.objects.filter(user__username=username).exists()

    if not profile_exists:
        # Si no existe el perfil, redirigir a la página de advertencia
        return redirect('no_freelancer_profile')

    # Obtener el perfil del freelancer
    profile = get_object_or_404(FreelancerProfile, user__username=username)

    # Obtener información relacionada con el freelancer
    skills = profile.skills.all()
    work_experiences = profile.user.work_experiences.all()
    portfolio_projects = PortfolioProject.objects.filter(profile=profile.user)
    curriculum = CurriculumVitae.objects.filter(profile=profile.user).first()
    courses = Course.objects.filter(profile=profile.user)

    context = {
        'profile': profile,
        'skills': skills,
        'work_experiences': work_experiences,
        'portfolio_projects': portfolio_projects,
        'curriculum': curriculum,
        'courses': courses,
    }

    return render(request, 'freelancer_profile_creation/freelancer_profile.html', context)



def no_freelancer_profile(request):
    return render(request, 'freelancer_profile_creation/no_freelancer_profile.html')

