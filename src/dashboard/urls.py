from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("project/", views.projects, name="projects"),
    path("chat/", views.chat, name="chat"),
    path("profile/", views.create_profile, name="profile"),
    path("settings/", views.settings, name="settings"),
    path("notifications/", views.notifications, name="notifications"),
    path("dashboard/", views.dashboard, name="dashboard"),  
    path("logout/", views.logout_view, name="logout"),       
    path("support/", views.logout_view, name="support"),    
]
