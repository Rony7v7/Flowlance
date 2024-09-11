from django.urls import path
from . import views

urlpatterns =[  path("", views.home, name="home"),
                path("projects/", views.projects, name="projects"),
                path("chat/", views.chat, name="chat"),
                path("profile/", views.profile, name="profile"),
                path("settings/", views.settings, name="settings"),
                path("notifications/", views.notifications, name="notifications"),
            ]
