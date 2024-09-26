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

from flowlance.decorators import attach_profile_info


@login_required
@attach_profile_info
def my_profile(request, username=None): 

    profile = request.profile
    profile_type = request.profile_type

    if profile_type == 'freelancer':
        return my_freelancer_profile(request, profile)
    elif profile_type == 'client':
        return my_client_profile(profile)
    else:
        return redirect('home')


def my_freelancer_profile(request, profile):
    try:
        portfolio = profile.portfolio_profile
        projects = portfolio.projects.all()
        courses = portfolio.courses.all()
           
    except Portfolio.DoesNotExist:
        portfolio = None
        projects = None
        courses = None

    ratings = Rating.objects.filter(freelancer=profile).order_by('-created_at')   

    context = {
        'profile': profile,
        'skills': profile.skills.all(),
        'experiences': profile.freelancer_work_experience.all(),
        'portfolio': portfolio,
        'projects': projects,
        'courses': courses,
        'ratings': ratings,
    }

    return render(request, 'profile/freelancer_profile.html', context)

def my_client_profile(request, profile):
    return redirect('home') # TODO: Redirect to the client profile view

@login_required
def notifications(request):
    notifications = request.user.notifications.filter(is_read=False)
    return render(request, 'profile/notifications.html', {'notifications': notifications})



