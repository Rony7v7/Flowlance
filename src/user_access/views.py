from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .login_form import login_form


class login_view(LoginView):
    template_name = "login/login.html"
    authentication_form = login_form
