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
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages", null=True, blank=True)  # El remitente del mensaje
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages", null=True, blank=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="messages",null=True, blank=True)  # El proyecto asociado
    content = models.TextField()  # El contenido del mensaje
    timestamp = models.DateTimeField(auto_now_add=True)  # Fecha y hora de envío del mensaje

    def __str__(self):
        return f"Message from {self.sender.username} to {self.recipient.username} at {self.timestamp}"

    

