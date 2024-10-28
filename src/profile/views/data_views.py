from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from ..forms import AddSkillsForm, AddWorkExperienceForm, UploadCVForm
from ..models import FreelancerProfile, CurriculumVitae, Portfolio, FreelancerProfile
from ..forms import AddProjectForm, AddCourseForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from ..models import Rating, RatingResponse
from ..forms import RatingForm, RatingResponseForm




@login_required
def add_course(request):
    profile = get_object_or_404(FreelancerProfile,user=request.user, is_deleted=False)
    FreelancerProfile.objects.get(user=request.user)
    
    portfolio, created = Portfolio.objects.get_or_create(freelancer_profile=profile)

    if request.method == 'POST':
        form = AddCourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.portfolio = portfolio  
            course.save()
            return redirect('my_profile')  
    else:
        form = AddCourseForm()

    return render(request, 'profile/add_course.html', {'form': form})


@login_required
def add_project(request):
    profile = get_object_or_404(FreelancerProfile,user=request.user,is_deleted=False)
    
    portfolio, created = Portfolio.objects.get_or_create(freelancer_profile=profile)

    if request.method == 'POST':
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = portfolio  
            project.save()
            return redirect('my_profile')  
    else:
        form = AddProjectForm()

    return render(request, 'profile/add_project.html', {'form': form})


@login_required
def upload_curriculum(request):
    profile = get_object_or_404(FreelancerProfile,user=request.user,is_deleted=False)
    try:
        curriculum = profile.freelancer_cv  
    except CurriculumVitae.DoesNotExist:
        curriculum = None  

    if request.method == 'POST':
        form = UploadCVForm(request.POST, request.FILES, instance=curriculum)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.profile = profile  
            cv.save()
            return redirect('my_profile')
    else:
        form = UploadCVForm(instance=curriculum)

    return render(request, 'profile/upload_curriculum.html', {'form': form})


@login_required
def freelancer_profile(request, username=None):
    if username is None:
        profile = get_object_or_404(FreelancerProfile,user=request.user,is_deleted=False)
    else:
        profile = get_object_or_404(FreelancerProfile, user__username=username,is_deleted=False)

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
        'profile': profile,
        'skills': profile.skills.filter(is_deleted=False),
        'experiences': profile.freelancer_work_experience.filter(is_deleted=False),
        'portfolio': portfolio,
        'projects': projects,
        'courses': courses,
        'ratings': ratings,
    }

    return render(request, 'profile/freelancer_profile.html', context)




@login_required
def customize_profile(request):
    user = request.user  
    
    if request.method == 'POST':
        form = AddSkillsForm(request.POST, user=user)  
        if form.is_valid():
            form.save(user=user)  
        return redirect('my_profile')
    else:
        form = AddSkillsForm(user=user)

    return render(request, 'profile/customize_profile.html', {'form': form})



@login_required
def add_experience(request):
    user = request.user
    
    if request.method == 'POST':
        form = AddWorkExperienceForm(request.POST)
        if form.is_valid():
            form.save(user=user)  
            return redirect('my_profile')  
    else:
        form = AddWorkExperienceForm()

    return render(request, 'profile/add_experience.html', {'form': form})

@login_required
def notifications(request):
    notifications = request.user.notifications.filter(is_read=False,is_deleted=False)
    return render(request, 'profile/notifications.html', {'notifications': notifications})

@login_required
def add_rating(request, freelancer_username):
    freelancer = get_object_or_404(FreelancerProfile, user__username=freelancer_username,is_deleted = False)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.freelancer = freelancer
            rating.client = request.user
            rating.save()
            messages.success(request, 'Your rating has been submitted successfully.')
            return redirect('my_profile', username=freelancer_username)
    else:
        form = RatingForm()
    return render(request, 'profile/add_rating.html', {'form': form, 'freelancer': freelancer})

@login_required
def add_rating_response(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id, freelancer__user=request.user,is_deleted=False)
    if request.method == 'POST':
        form = RatingResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.rating = rating
            response.save()
            messages.success(request, 'Your response has been added successfully.')
            return redirect(reverse('my_profile', kwargs={'username': request.user.username}))
    else:
        form = RatingResponseForm()
    return render(request, 'profile/add_rating_response.html', {'form': form, 'rating': rating})

@login_required
def edit_rating_response(request, response_id):
    response = get_object_or_404(RatingResponse, id=response_id, rating__freelancer__user=request.user,is_deleted=False)
    if not response.can_edit():
        messages.error(request, 'You can no longer edit this response.')
        return redirect(reverse('my_profile', kwargs={'username': request.user.username}))
    
    if request.method == 'POST':
        form = RatingResponseForm(request.POST, instance=response)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your response has been updated successfully.')
            return redirect(reverse('my_profile', kwargs={'username': request.user.username}))
    else:
        form = RatingResponseForm(instance=response)
    return render(request, 'profile/edit_rating_response.html', {'form': form, 'response': response})

@require_POST
@login_required
def delete_rating_response(request, response_id):
    response = get_object_or_404(RatingResponse, id=response_id,is_deleted = False)
    if request.user == response.rating.client or request.user.is_superuser:
        response.is_deleted = True
        response.save()
        messages.success(request, 'Respuesta eliminada correctamente.')
    else:
        messages.error(request, 'No tienes permisos para eliminar esta respuesta.')
    return redirect('my_profile')  # Ajusta según la página de redirección

@require_POST
@login_required
def delete_rating(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)
    if request.user == rating.client or request.user.is_superuser:
        rating.is_deleted = True
        rating.save()
        messages.success(request, 'Calificación eliminada correctamente.')
    else:
        messages.error(request, 'No tienes permisos para eliminar esta calificación.')
    return redirect('my_profile')  # Ajusta según la página de redirección
