from django.shortcuts import render, redirect

from email_service.email_service import send_email
from .LoginForm import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django_otp.oath import TOTP
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

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
                # Genera un código OTP temporal
                totp = TOTP(key=username.encode(), step=300)  # Valido por 5 minutos
                otp_code = totp.token()

                # Envía el OTP al email del usuario
                send_email(
                    user.username,
                    _("Codigo de verificacion"),
                    str(otp_code),
                    _("Codigo de verificacion: "),
                    _("Si este codigo no lo solicito porfavor haga caso omiso y considere cambiar sus credenciales"),
                )
                # Guarda el usuario en la sesión (sin hacer login todavía)
                request.session["pre_otp_user"] = user.id
                return redirect("/two_factor_auth/")
            else:
                messages.error(request, _("Invalid username or password."))
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
