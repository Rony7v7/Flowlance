from django.urls import re_path , path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server/',consumers.NotificationConsumer.as_asgi()),
    path("ws/notifications/<str:username>",consumers.NotificationConsumer.as_asgi())
]