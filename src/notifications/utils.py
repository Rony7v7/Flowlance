from django.contrib.auth.models import User
from .models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from email_service.email_service import send_email
from django.utils.translation import gettext as _
from profile.models import ProfileConfiguration
from datetime import datetime
# Please use this function every time you want to send a notification
# The link of creation is where the notification is comming from, a dashboard, a proyect , a message?

#to use the notification type you can just use Notification.NotificationType.TYPE, type being either peojct, paymen tor message

#By default it will de other
def send_notification(title, notification_message, link_of_creation, user_Receiver,notification_type = Notification.NotificationType.OTHER):

    user = User.objects.get(username=user_Receiver)

    pref = ProfileConfiguration.objects.filter(username=user_Receiver).first()
    
    if pref and pref.silent_start and pref.silent_end:
        now = datetime.now().time()
        # Check if current time is within silent hours
        if pref.silent_start <= now <= pref.silent_end:
            return  # Don't send notifications during silent hours

    notification = Notification.objects.create(
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

    profile , profile_type = user_Receiver.get_profile_info()

    if profile and profile.profileconfiguration: #There mught be a case where the userd doesnt have a profile
        if profile.profileconfiguration.sending_notification_to_email: #This check if the notification should be sent to the email
            email_subject = _("Nueva Notificacion")
            email_body = f"""

                    {notification.message}

                    Puede ver mas informacion en el siguiente enlace: 

                    {notification.link_to_place_of_creation}
                    """
            email_title = _(f"Nueva notificacion de {notification.notification_type.name}")
            
            async_to_sync(send_email(user_Receiver.email,email_subject,_(email_body),email_title))