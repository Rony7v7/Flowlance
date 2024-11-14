from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from ..models import CompanyProfile, Portfolio, Rating
from django.contrib import messages
from ..forms import CompanyProfileForm, ProfileConfigurationForm
from notifications.utils import send_notification
from ..models import ProfileConfiguration
from django.utils.translation import gettext as _
from datetime import datetime

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

    if request.profile.profileconfiguration.notification_when_profile_visited:
        notification_title = _("Perfil visualizado")
        now = datetime.now()
        notification_message = _(f"Su perfil ha sido visualizado por el cliente {request.user.username}, a las {now.strftime('%d/%m/%Y %H:%M:%S')}")
        notification_link = reverse("my_profile")
        send_notification(notification_title,notification_message,notification_link,request.profile.user) 

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

    ratings = Rating.objects.filter(freelancer=profile).order_by('-created_at')

    for rating in ratings:
        rating.star_range = range(rating.stars)

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
@attach_profile_info
def notifications(request):
    notifications = request.user.notifications.filter(is_deleted=False)
    return render(request, 'profile/notifications.html', {'notifications': notifications, 'section': 'notifications'})

@login_required
@attach_profile_info
def notification_preferences(request):
    # Get the user's profile and profile configuration
    try:
        # Assuming users can have either a FreelancerProfile or CompanyProfile
        if hasattr(request.user, 'freelancerprofile'):
            profile = request.user.freelancerprofile
        elif hasattr(request.user, 'companyprofile'):
            profile = request.user.companyprofile
        else:
            # If neither profile exists, redirect or raise an error
            messages.error(request, "Profile not found.")
            return redirect('home')

        # Get or create the ProfileConfiguration associated with the profile
        profile_config, created = ProfileConfiguration.objects.get_or_create(
            id=profile.profileconfiguration.id if profile.profileconfiguration else None,
            defaults={'notification_when_profile_visited': True}
        )
        if created:
            profile.profileconfiguration = profile_config
            profile.save()

    except ProfileConfiguration.DoesNotExist:
        messages.error(request, "Unable to access notification preferences.")
        #! Redirect to home or another page
        return redirect('home')

    # Handle form submission
    if request.method == 'POST':
        form = ProfileConfigurationForm(request.POST, instance=profile_config)
        if form.is_valid():
            form.save()
            messages.success(request, 'Preferences updated successfully.')
            return redirect('notification_preferences')
    else:
        form = ProfileConfigurationForm(instance=profile_config)

    preview = {
        "periodicity_of_notification_report": profile_config.periodicity_of_notification_report,
        "notification_when_profile_visited": profile_config.notification_when_profile_visited,
        "sending_notification_to_email": profile_config.sending_notification_to_email,
        "receive_project_updates": profile_config.receive_project_updates,
        "receive_messages": profile_config.receive_messages,
        "receive_job_opportunities": profile_config.receive_job_opportunities,
        "silent_start": profile_config.silent_start,
        "silent_end": profile_config.silent_end,
        
    }
    
    return render(request, 'profile/notification_preferences.html', {'form': form, 'preview': preview})
@login_required
@attach_profile_info
def reset_notification_preferences(request):
    try:
        # Check if the user has either a FreelancerProfile or CompanyProfile
        if hasattr(request.user, 'freelancerprofile'):
            profile = request.user.freelancerprofile
        elif hasattr(request.user, 'companyprofile'):
            profile = request.user.companyprofile
        else:
            messages.error(request, "Profile not found.")
            #! Redirect to home or another page
            return redirect('home')

        # Get the ProfileConfiguration associated with the profile
        profile_config = profile.profileconfiguration
        if not profile_config:
            messages.error(request, "Notification preferences not found.")
            return redirect('notification_preferences')

        # Reset the preferences
        profile_config.receive_project_updates = True
        profile_config.receive_messages = False
        profile_config.receive_job_opportunities = True
        profile_config.silent_start = None
        profile_config.silent_end = None
        profile_config.save()
        
        messages.success(request, 'Preferences reset to default values.')

    except ProfileConfiguration.DoesNotExist:
        messages.error(request, "Unable to reset preferences.")
    
    return redirect('notification_preferences')

@login_required
def update_company_profile(request):
    try:
        company_profile = request.user.companyprofile
    except CompanyProfile.DoesNotExist:
        messages.error(request, "No tienes un perfil de compañía creado.")
        return redirect('home')

    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, instance=company_profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect('my_profile')
        else:
            messages.error(request, "Error al actualizar el perfil. Revisa los datos.")
    else:
        form = CompanyProfileForm(instance=company_profile, user=request.user)

    return render(request, 'update_profile.html', {'form': form})
