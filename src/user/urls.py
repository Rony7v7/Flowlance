from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'), 
    
]
