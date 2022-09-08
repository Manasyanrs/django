from django.urls import path
from .views import LogInViews, LogOutView


urlpatterns = [
    path("login/", LogInViews.as_view(), name="login_user"),
    path("logout/", LogOutView.as_view(), name="logout_user"),

]

