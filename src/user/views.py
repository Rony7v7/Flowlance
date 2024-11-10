from django.shortcuts import render, redirect

from email_service.email_service import send_email

from .LoginForm import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django_otp.oath import TOTP
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .RestorePasswordForm import StyledPasswordChangeForm
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialAccount

def home(request):
    return render(request, "homepage/home.html")


def choose_path_view(request):
    return render(request, "navigation/choose_path.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Access the user's profile information
                profile, profile_type = user.get_profile_info()

                # Check if the user has Two-Factor Authentication (2FA) enabled
                if profile and profile.has_2FA_on:
                    # Generate an OTP (One-Time Password) for users with 2FA enabled
                    totp = TOTP(key=username.encode(), step=300)  # Valid for 5 minutes
                    otp_code = totp.token()

                    # Send the OTP code to the user's email
                    send_email(
                        user.username,
                        _("Verification Code"),
                        str(otp_code),
                        _("Your verification code is: "),
                        _("If you did not request this, please ignore it and consider changing your credentials."),
                    )

                    # Store the user in session temporarily until 2FA is verified
                    request.session["pre_otp_user"] = user.id
                    return redirect("/two_factor_auth/")  # Redirect to OTP verification page
                else:
                    # If no 2FA, log the user in directly
                    login(request, user)
                    return redirect("/dashboard/")  # Redirect to homepage or another page after login
            else:
                messages.error(request, _("Por favor revise su usuario y contraseña"))
        else:
            messages.error(request, _("Por favor revise su usuario y contraseña"))
    else:
        form = LoginForm()

    return render(request, "login/login.html", {"form": form})



def two_factor_validator(request):
    if request.method == "POST":
        otp_input = request.POST.get("otp-code")

        # Recupera el usuario almacenado temporalmente en la sesión
        user_id = request.session.get("pre_otp_user")
        if not user_id:
            return redirect("login/")  # Si no hay usuario en sesión, redirige a login

        user = User.objects.get(id=user_id)
        totp = TOTP(
            key=user.username.encode(), step=300
        )  # Misma configuración que antes
        try:
            if totp.verify(int(otp_input), tolerance=1):
                # El OTP es válido, hacer login del usuario
                del request.session["pre_otp_user"]  # Limpia la sesión
                login(request, user)
                return redirect("/dashboard/")
            else:
                return render(
                    request, "login/2_factor_auth.html", {"error": _("OTP incorrecto")}
                )
        except:
            return render(
                request, "login/2_factor_auth.html", {"error": _("OTP incorrecto")}
            )
    return render(request, "login/2_factor_auth.html", {})


@login_required
def restore_password(request):
    if request.method == "POST":
        form = StyledPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Se ha actualizado con exito'))
            return redirect('security_settings')
    else:
        form = StyledPasswordChangeForm(request.user)

    return render(request, 'settings/restore_password.html', {
        'form': form
    })


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
                return redirect('dashboard') 
        except User.DoesNotExist:
            # No user with this email exists, redirect to registration
            return redirect('register')
    else:
        # User logged in with username/password
        if hasattr(user, 'profile'):
            return redirect('dashboard')
        else:
            return redirect('choose_path')





