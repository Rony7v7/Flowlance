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
            experience.freelancer = request.user.freelancerprofile  
            experience.save()
            return redirect('freelancer_own_profile')  
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
            proyecto.profile = request.user.freelancerprofile  # Now linked to FreelancerProfile
            proyecto.save()
            return redirect('upload_curriculum')  
    else:
        form = PortfolioProjectForm()
    return render(request, 'freelancer_profile_creation/create_project_portfolio.html', {'form': form})



@login_required
def upload_curriculum(request):
    try:
        curriculum = CurriculumVitae.objects.get(profile=request.user.freelancerprofile)
    except CurriculumVitae.DoesNotExist:
        curriculum = None

    if request.method == 'POST':
        form = CurriculumVitaeForm(request.POST, request.FILES, instance=curriculum)
        if form.is_valid():
            curriculum = form.save(commit=False)
            curriculum.profile = request.user.freelancerprofile  # Now linked to FreelancerProfile
            curriculum.save()
            return redirect('add_course')  
    else:
        form = CurriculumVitaeForm(instance=curriculum)
    
    return render(request, 'freelancer_profile_creation/upload_curriculum.html', {'form': form})


@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.profile = request.user.freelancerprofile  # Now linked to FreelancerProfile
            curso.save()
            return redirect('freelancer_profile', username=request.user.username)  
    else:
        form = CourseForm()
    return render(request, 'freelancer_profile_creation/add_course.html', {'form': form})

@login_required
def freelancer_own_profile(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    
    try:
        profile = request.user.freelancerprofile
    except FreelancerProfile.DoesNotExist:
        return redirect('no_freelancer_profile')

    skills = profile.skills.all()
    work_experiences = profile.work_experiences.all()
    portfolio_projects = profile.freelancer_portfolio_projects.all()

    curriculum = None
    try:
        curriculum = profile.freelancer_cv
    except CurriculumVitae.DoesNotExist:
        pass  
    
    courses = profile.freelancer_courses.all()

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
    profile_exists = FreelancerProfile.objects.filter(user__username=username).exists()

    if not profile_exists:
        return redirect('no_freelancer_profile')

    profile = get_object_or_404(FreelancerProfile, user__username=username)

    skills = profile.skills.all()  
    work_experiences = profile.work_experiences.all()  
    portfolio_projects = profile.portfolio_projects.all()
    curriculum = profile.curriculum_vitae  
    courses = profile.courses.all() 

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

