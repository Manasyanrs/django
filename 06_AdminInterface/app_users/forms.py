from django import forms
from .models import Login


class LogInForm(forms.Form):
    model = Login
    username = forms.CharField(label="Логин")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
