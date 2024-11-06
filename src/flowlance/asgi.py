"""
ASGI config for flowlance project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import notifications.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowlance.settings')

#Esto le dice a django que utilizar para routear las diferentes requests, en nuestros caso viene siendo http y websockets
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(notifications.routing.websocket_urlpatterns)
    )
}) 
