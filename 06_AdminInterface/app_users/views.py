from django.contrib.auth.views import LoginView, LogoutView


class LogInViews(LoginView):
    template_name = "app_users/login.html"


class LogOutView(LogoutView):
    template_name = "app_users/logout.html"
