import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.urls import reverse
from .models import Message
from django.contrib.auth.models import User
from project.models import Project
from notifications.utils import send_notification
from django.utils.translation import gettext as _
from notifications.models import Notification

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.project_id = self.scope['url_route']['kwargs']['project_id']
        self.recipient_id = self.scope['url_route']['kwargs']['recipient_id']

        # Definir el room_group_name de manera que ambos usuarios estén en el mismo grupo
        self.room_group_name = f"chat_{self.project_id}_{min(self.scope['user'].id, int(self.recipient_id))}_{max(self.scope['user'].id, int(self.recipient_id))}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender_id = data['sender_id']
        recipient_id = data['recipient_id']
        project_id = data['project_id']

        # Guardar el mensaje en la base de datos
        sender = await sync_to_async(User.objects.get)(id=sender_id)
        recipient = await sync_to_async(User.objects.get)(id=recipient_id)
        project = await sync_to_async(Project.objects.get)(id=project_id)
        notification_subject = _("Nuevo Mensaje")
        notification_body = _(f"Tiene un nuevo mensaje de {sender}: \n {message}")
        notification_link = reverse("chat_overview")
        send_notification(notification_subject,notification_body,notification_link,recipient,notification_type=Notification.NotificationType.MESSAGE)

        # Crear el mensaje en la base de datos
        await sync_to_async(Message.objects.create)(
            sender=sender,
            recipient=recipient,
            project=project,
            content=message
        )

        # Enviar el mensaje a todos en el room_group_name, incluido el remitente y el destinatario
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': sender.username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        await self.send(text_data=json.dumps({
            'message': message,
            'user': user
        }))
