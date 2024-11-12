from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Notification
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from collections import Counter
from email_service.email_service import send_email
from django.contrib import messages
from django.utils.translation import gettext as _

# Create your views here.

def notifications(request):
    return render(request, "navigation/building.html")

@login_required
def mark_notification_as_read(request, notification_id):
    if request.method == "POST":
        # Fetch the notification or return a 404 if it doesn't exist
        notification = get_object_or_404(Notification, id=notification_id)
        
        # Mark the notification as read
        notification.is_read = True
        notification.save()
        
        # Return a success response
        return JsonResponse({"status": "success", "message": "Notification marked as read."})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

@login_required
def mark_all_notifications_as_read(request):
    if request.method == "POST":
        # Update all unread notifications for the user in a single query
        updated_count = Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        
        # Return a JSON response indicating the number of notifications updated
        return redirect('notifications')
    else:
        return redirect('notifications')


@login_required
def delete_notification(request, notification_id):
 # Get the notification or return a 404 if it doesn't exist
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)

    # If request is POST, delete the notification
    if request.method == "POST":
        notification.delete()
        return JsonResponse({"status": "success", "message": "Notification deleted successfully."})
    
    # If request method is not POST, return a 405 error
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

@login_required
def create_report_notifications(request):
    user = request.user
    profile, profile_type = user.get_profile_info()
    profile_config = profile.profileconfiguration

    # Fetch notifications for the user within the selected period
    notifications = Notification.objects.filter(
        user=user,
        is_deleted=False
    )

    # Count notifications by type
    notification_counts = Counter(notif.notification_type for notif in notifications)

    # Organize the summary content
    summary = []
    for notif_type, count in notification_counts.items():
        notification_type_display = Notification.NotificationType(notif_type).label
        summary.append({
            "type": notification_type_display,
            "count": count,
            "link": reverse('notifications') 
        })

    for notif in notifications:
        summary.append({
            "type": notif.get_notification_type_display(),
            "title": notif.title,
            "message": notif.message,
            "link": notif.link_to_place_of_creation,
            "created_at": notif.created_at.strftime("%Y-%m-%d %H:%M"),
        })

    # Render email content
    email_subject = "Resumen de Notificaciones Importantes"
    email_content = render_to_string('emails/notification_summary.html', {
        'user': user,
        'summary': summary,
    })

    send_email(request.user.email,email_subject,email_content)

    # Provide feedback to the user (optional, as this might be an automated job)
    messages.success(request, _("Resumen de notificaciones enviado a su correo electrónico."))

    #No tiene return porque no deberia retornar nada
    return HttpResponse(200)
