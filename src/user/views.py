from django.shortcuts import render, redirect

from profile.forms import FreelancerRegisterForm
from .LoginForm import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialAccount

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


def success_or_not(request):
    return render(request, "login/success_or_not.html")

@login_required
def check_profile(request):
    user = request.user
    User = get_user_model()

    # Check if the user logged in with Google
    try:
        google_login = user.socialaccount_set.get(provider='google')
    except SocialAccount.DoesNotExist:
        google_login = None

    if google_login:
        # User logged in with Google
        try:
            # Check if a user with this email already exists
            existing_user = User.objects.get(email=user.email)
            if existing_user != user:
                # If a different user with this email exists, handle the conflict
                # For example, you might want to merge accounts or show an error
                return redirect('success_or_not')
            
            # User exists, check if they have a profile
            if hasattr(existing_user, 'profile'):
                return redirect('dashboard')
            else:
                return redirect('dashboard') #acaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        except User.DoesNotExist:
            # No user with this email exists, redirect to registration
            return redirect('register')
    else:
        # User logged in with username/password
        if hasattr(user, 'profile'):
            return redirect('dashboard')
        else:
            return redirect('choose_path')





