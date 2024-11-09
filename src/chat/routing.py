from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<project_id>\d+)_(?P<recipient_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
]
