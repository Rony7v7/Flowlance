##Estas son como las views pero de los websockets, es lo que se llama cuando llega un mensaje
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username = self.scope['url_route']['kwargs']['username']
        self.group_name = f'notifications_{self.username}'
        # Únete al grupo de notificaciones del usuario
        await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )

        await self.accept()

    async def disconnect(self, close_code):
        # Sal del grupo de notificaciones
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Recibe mensaje desde el grupo de WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        notification = text_data_json['message']

        # Enviar notificación al cliente WebSocket
        await self.send(text_data=json.dumps({
            'message': notification
        }))

   # Este método recibe el evento y envía la notificación al WebSocket
    async def send_notification(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'type': "new_notification",
            'message': message
        }))
