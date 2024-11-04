from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from profile.models import FreelancerProfile, FreelancerProfile, Rating, RatingResponse
from profile.forms import RatingForm, RatingResponseForm

from notifications.utils import send_notification
from django.utils.translation import gettext as _


@login_required
def add_rating(request, freelancer_username):

    freelancer = get_object_or_404(FreelancerProfile, user__username=freelancer_username,is_deleted=False)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.freelancer = freelancer
            rating.client = request.user
            rating.save()
            notification_message = _("Has recibido una nueva calificación de {request.user.username}.")
            notification_title = _("Nueva Calificacion")
            notification_link = reverse('freelancer_profile', kwargs={'username': freelancer_username})
            send_notification(notification_title,notification_message ,notification_link, request.user)
            # Notificar al freelancer que ha recibido una nueva calificación

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success'}, status=200)
            else:
                messages.success(request, 'Tu calificación ha sido enviada exitosamente.')
                return redirect('freelancer_profile', username=freelancer_username)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'errors': form.errors}, status=400)
            else:
                messages.error(request, 'Error al enviar la calificación.')
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

            notification_message = _("{request.user.username} ha respondido a tu calificación.")
            notification_title = _("Respuesta a Calificacion")
            notification_link = reverse('freelancer_profile', kwargs={'username': request.user.username})
            send_notification(notification_title,notification_message ,notification_link, request.user)

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)



@login_required
def edit_rating_response(request, response_id):

    response = get_object_or_404(RatingResponse, id=response_id, rating__freelancer__user=request.user,is_deleted=False)
    if not response.can_edit():
        messages.error(request, 'You can no longer edit this response.')
        return redirect(reverse('freelancer_profile', kwargs={'username': request.user.username}))

    if request.method == 'POST':
        form = RatingResponseForm(request.POST, instance=response)
        if form.is_valid():
            form.save()
            notification_message = _("{request.user.username} ha editado la respuesta de la calificación.")
            notification_title = _("Edicion de calificacion")
            notification_link = reverse('freelancer_profile', kwargs={'username': request.user.username})
            send_notification(notification_title,notification_message,notification_link, request.user)

            messages.success(request, 'Respuesta editada con éxito.')
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = RatingResponseForm(instance=response)
    
    return render(request, 'profile/edit_rating_response.html', {'form': form, 'response': response})


@login_required
def get_rating_response(request, response_id):
    response = get_object_or_404(RatingResponse, id=response_id)
    return JsonResponse({'response_text': response.response_text})

    


@login_required
@require_POST
def delete_rating(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id,is_deleted=False)
    if request.method == "POST":
        rating.is_deleted = True
        rating.save()
        return redirect('freelancer_profile', username=rating.freelancer.user.username)


@login_required
@require_POST
def delete_rating_response(request, response_id):
    response = get_object_or_404(RatingResponse, id=response_id)
    response.delete()
    return redirect('freelancer_profile',username=request.user.username)










