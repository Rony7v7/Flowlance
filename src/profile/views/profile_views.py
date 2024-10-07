from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from ..forms import AddSkillsForm, AddWorkExperienceForm, UploadCVForm
from ..models import FreelancerProfile, CurriculumVitae, Portfolio, FreelancerProfile, Notification
from ..forms import AddProjectForm, AddCourseForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from ..models import Rating, RatingResponse
from ..forms import RatingForm, RatingResponseForm

from flowlance.decorators import attach_profile_info, client_required
from django.contrib.auth.models import User


@login_required
@attach_profile_info
def my_profile(request): 

    profile = request.profile
    profile_type = request.profile_type

    if profile_type == 'freelancer':
        return my_freelancer_profile(request, profile)
    elif profile_type == 'company':
        return my_company_profile(request, profile)
    else:
        return redirect('home')

@login_required
@attach_profile_info
def my_freelancer_profile(request):
    profile = request.profile

    context = generate_freelancer_context(profile)
    context['is_owner'] = True

    return render(request, 'profile/freelancer_profile.html', context)

@login_required
@attach_profile_info
def my_company_profile(request):
    profile = request.profile  
    context = generate_company_context(profile)
    context['is_owner'] = True 
    return render(request, 'profile/company_profile.html', context)

def generate_company_context(profile):
    """Genera el contexto para el perfil de la compañía."""
    context = {
        'company_name': profile.company_name,
        'nit': profile.nit,
        'business_type': profile.business_type,
        'country': profile.country,
        'business_vertical': profile.business_vertical,
        'address': profile.address,
        'legal_representative': profile.legal_representative,
        'phone': profile.phone,
        'photo': profile.photo,
    }
    return context


@login_required
@attach_profile_info
@client_required
def freelancer_profile_view(request, username):

    if request.user.username == username:
        return redirect('my_profile')

    # Search for the user
    user = get_object_or_404(User, username=username)
    
    request.profile, request.profile_type = user.get_profile_info()

    context = generate_freelancer_context(request.profile)
    context['is_owner'] = False
    context['viewer'] = request.user

    return render(request, 'profile/freelancer_profile.html', context)

def generate_freelancer_context(profile):
    try:
        portfolio = profile.portfolio_profile
        projects = portfolio.projects.filter(is_deleted=False)
        courses = portfolio.courses.filter(is_deleted=False)
           
    except Portfolio.DoesNotExist:
        portfolio = None
        projects = None
        courses = None

    ratings = Rating.objects.filter(freelancer=profile,is_deleted=False).order_by('-created_at')   

    context = {
        'skills': profile.skills.filter(is_deleted=False),
        'experiences': profile.freelancer_work_experience.filter(is_deleted=False),
        'portfolio': portfolio,
        'projects': projects,
        'courses': courses,
        'ratings': ratings,
    }

    return context

@login_required
def notifications(request):
    notifications = request.user.notifications.filter(is_read=False)
    return render(request, 'profile/notifications.html', {'notifications': notifications})



