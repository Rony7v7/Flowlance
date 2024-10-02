from django.shortcuts import render, redirect
from .LoginForm import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def home(request):
    return render(request, "homepage/home.html")


def choose_path_view(request):
    return render(request, 'navigation/choose_path.html')  


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/dashboard/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Por favor revise su usuario y contraseña")
    else:
        form = LoginForm()
    return render(request, "login/login.html", {"form": form})
