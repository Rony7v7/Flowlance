from django.contrib.auth.models import User
from .models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_notification(notification_message, user_Receiver):
    user = User.objects.get(username=user_Receiver)

    Notification.objects.create(user=user_Receiver, message=notification_message)

    channel_layer = get_channel_layer()
    group_name = f'notifications_{user.username}'

    # Utiliza async_to_sync para llamar al método asincrónico desde un contexto sincrónico
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'send_notification',
            'message': notification_message
        }
    )
