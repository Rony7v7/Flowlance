from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("choose-path/", views.choose_path_view, name="choose_path"),
    path("two_factor_auth/", views.two_factor_validator, name="two_factor_validator"),
    path("restore_password/",views.restore_password, name = "restore_password"),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'), 
    path('choose-path/', views.choose_path_view, name='choose_path'), 
    path('check-profile/', views.check_profile, name='check_profile'),
    path('success-or-not/', views.success_or_not, name='success_or_not'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="login/password_reset_form.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="login/password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="login/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="login/password_reset_complete.html"), name='password_reset_complete'),
]
