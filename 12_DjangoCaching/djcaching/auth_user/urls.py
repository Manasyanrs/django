from django.urls import path
from .views import LogInViews, RegisterUser
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", LogInViews.as_view(), name="login_user"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout_user"),
    path("register/", RegisterUser.as_view(), name="register_user"),
]
