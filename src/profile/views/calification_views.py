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

@login_required
def add_rating(request, freelancer_username):
    freelancer = get_object_or_404(FreelancerProfile, user__username=freelancer_username)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.freelancer = freelancer
            rating.client = request.user
            rating.save()

            # Notificar al freelancer que ha recibido una nueva calificación
            Notification.objects.create(
                user=freelancer.user,
                message=f"Has recibido una nueva calificación de {request.user.username}."
            )

            messages.success(request, 'Your rating has been submitted successfully.')
            return redirect('freelancer_profile', username=freelancer_username)
    else:
        form = RatingForm()
    return render(request, 'profile/add_rating.html', {'form': form, 'freelancer': freelancer})



@login_required
def add_rating_response(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id, freelancer__user=request.user)
    if request.method == 'POST':
        form = RatingResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.rating = rating
            response.save()

            # Notificar al cliente que su calificación ha recibido una respuesta
            Notification.objects.create(
                user=rating.client,
                message=f"{request.user.username} ha respondido a tu calificación."
            )

            messages.success(request, 'Your response has been added successfully.')
            return redirect(reverse('freelancer_profile', kwargs={'username': request.user.username}))
    else:
        form = RatingResponseForm()
    return render(request, 'profile/add_rating_response.html', {'form': form, 'rating': rating})


@login_required
def edit_rating_response(request, response_id):
    response = get_object_or_404(RatingResponse, id=response_id, rating__freelancer__user=request.user)
    if not response.can_edit():
        messages.error(request, 'You can no longer edit this response.')
        return redirect(reverse('freelancer_profile', kwargs={'username': request.user.username}))
    
    if request.method == 'POST':
        form = RatingResponseForm(request.POST, instance=response)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your response has been updated successfully.')
            return redirect(reverse('freelancer_profile', kwargs={'username': request.user.username}))
    else:
        form = RatingResponseForm(instance=response)
    return render(request, 'profile/edit_rating_response.html', {'form': form, 'response': response})
    


@login_required
@require_POST
def delete_rating(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)
    if request.method == "POST":
        rating.delete()
        return redirect('freelancer_profile', username=rating.freelancer.user.username)


@login_required
@require_POST
def delete_rating_response(request, response_id):
    response = get_object_or_404(RatingResponse, id=response_id)
    response.delete()
    return redirect('freelancer_profile')









