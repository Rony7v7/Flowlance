from django.db import models
from django.contrib.auth.models import User
from project.models import Project  # Asegúrate de importar el modelo de proyecto

class ChatRoom(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="chat_rooms")
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat Room for {self.project.title}"

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}..."
    

