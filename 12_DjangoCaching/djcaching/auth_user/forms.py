from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Login


class LogInForm(forms.Form):
    model = Login
    username = forms.CharField(label="Логин")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=23, required=True)
    last_name = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(max_length=35, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")


class LoginForm(AuthenticationForm):
    fields = ('username', 'password')
