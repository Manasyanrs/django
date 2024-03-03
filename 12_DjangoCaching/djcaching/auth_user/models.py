from django.contrib.auth.models import User
from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=25, default="", db_index=True, verbose_name="username")
    password = models.CharField(max_length=25, default="", verbose_name="password")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    verification_flag = models.BooleanField(default=False, verbose_name="verification_flag")

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        db_table = "Profile"
        verbose_name = "user data"
        verbose_name_plural = "additional user data"
