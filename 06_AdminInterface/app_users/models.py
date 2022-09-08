from django.db import models
from django.urls import reverse


class Login(models.Model):
    username = models.CharField(max_length=25, default="", db_index=True, verbose_name="имя пользователя")
    password = models.CharField(max_length=25, default="", verbose_name="пароль пользователя")

    def __str__(self):
        return "{} {}".format(self.username, self.password)

    def get_absolute_url(self):
        return reverse("all_news")

    class Meta:
        db_table = "User"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователь"
