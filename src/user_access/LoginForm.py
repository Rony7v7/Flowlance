from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control w-full rounded-md bg-bg-white border border-primary_lightest",
            }
        ),
        error_messages={"required": "Username is empty"},
        label="Email / NIT",
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control w-full rounded-3xl bg-bg-white border rounded-md border-primary_lightest",
            }
        ),
        error_messages={"required": "Password is empty"},
        label="Contraseña",
    )
