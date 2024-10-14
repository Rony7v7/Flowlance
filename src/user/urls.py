from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("choose-path/", views.choose_path_view, name="choose_path"),
    path("two_factor_auth/", views.two_factor_validator, name="two_factor_validator"),
    path("restore_password/",views.restore_password, name = "restore_password")
]
