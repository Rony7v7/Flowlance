from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    link_to_place_of_creation = models.CharField(max_length=255) #This link is supposed to take you to the place where the notification was created
    #so it can be chats, a proyect o the dasboard to see the payment
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"

    def can_edit(self):
        return timezone.now() - self.created_at < timezone.timedelta(hours=24)