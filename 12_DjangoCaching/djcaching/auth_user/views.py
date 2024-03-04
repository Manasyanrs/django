from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .forms import RegisterForm, LoginForm
from .models import Profile


class LogInViews(LoginView):
    template_name = "auth_user/login.html"
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.form_valid(form)
            return HttpResponseRedirect("/")
        return render(request, "auth_user/login.html", {"form": form})


class RegisterUser(View):
    template_name = "auth_user/register.html"

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, "auth_user/register.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email,
                                            password=password)
            Profile.objects.create(user=user)
            username = form.cleaned_data["email"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            form = RegisterForm()
        return render(request, "auth_user/register.html", {"form": form})
