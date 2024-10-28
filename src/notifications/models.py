from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"

    def can_edit(self):
        return timezone.now() - self.created_at < timezone.timedelta(hours=24)