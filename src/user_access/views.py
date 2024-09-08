from django.shortcuts import render, redirect
from .LoginForm import LoginForm
from django.contrib.auth import login


def home(request):
    return render(request, "homepage/home.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm()
    return render(request, "login/login.html", {"form": form})
