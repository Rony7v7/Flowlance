from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control w-full block", "placeholder": "Username"}
        ),
        error_messages={"required": "Username is empty"},
        label="Email/NIT",
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control block w-full", "placeholder": "Password"}
        ),
        error_messages={"required": "Password is empty"},
        label="Contrasenia",
    )
