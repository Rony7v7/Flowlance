from django.contrib.auth.models import User
from .models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


# Please use this function every time you want to send a notification
# The link of creation is where the notification is comming from, a dashboard, a proyect , a message?

#to use the notification type you can just use Notification.NotificationType.TYPE, type being either peojct, paymen tor message

#By default it will de other
def send_notification(title, notification_message, link_of_creation, user_Receiver,notification_type = Notification.NotificationType.OTHER):
    user = User.objects.get(username=user_Receiver)

    Notification.objects.create(
        title=title,
        user=user_Receiver,
        message=notification_message,
        link_to_place_of_creation=link_of_creation,
        notification_type = notification_type
    )

    channel_layer = get_channel_layer()
    group_name = f"notifications_{user.username}"

    # Utiliza async_to_sync para llamar al método asincrónico desde un contexto sincrónico
    async_to_sync(channel_layer.group_send)(
        group_name, {"type": "send_notification", "message": notification_message}
    )
