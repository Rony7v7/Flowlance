from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'), 
    path('choose-path/', views.choose_path_view, name='choose_path'), 
    path('check-profile/', views.check_profile, name='check_profile'),
    path('success-or-not/', views.success_or_not, name='success_or_not'),
]
