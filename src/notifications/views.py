from django.shortcuts import get_object_or_404, render
from .models import Notification
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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
        return JsonResponse({"status": "success", "updated_count": updated_count})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)


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
