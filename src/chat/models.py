from django.db import models
from django.contrib.auth.models import User
from project.models import Project  # Asegúrate de importar el modelo de proyecto

class ChatRoom(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="chat_rooms")
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat Room for {self.project.title}"

# models.py
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages", null=True, blank=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="messages", null=True, blank=True)
    content = models.TextField(blank=True)  # Permitir mensajes sin texto
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='chat_files/', null=True, blank=True)  # Nuevo campo para archivos
    hidden_for_sender = models.BooleanField(default=False)
    hidden_for_recipient = models.BooleanField(default=False)

    def __str__(self):
        if self.file:
            return f"File message from {self.sender.username} to {self.recipient.username} at {self.timestamp}"
        return f"Message from {self.sender.username} to {self.recipient.username} at {self.timestamp}"
