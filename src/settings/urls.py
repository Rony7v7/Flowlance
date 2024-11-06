from django.urls import path, include
from . import views

urlpatterns = [
    path("account_settings", views.settings, name="account_settings"),
    path("security_settings", views.security_settings, name="security_settings"),
    path("toggle_2fa/", views.toggle_2fa, name="toggle_2fa"),
    path("toggle_notification_when_profile_visited", views.toggle_notification_when_profile_visited,name = "toggle_notification_when_profile_visited")
]
