from django.db import models
from django.urls import reverse
from django.contrib import admin
from app_users.models import Login


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    count_of_employers = models.IntegerField()
    director = models.CharField(max_length=30)
    chef = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house = models.IntegerField()
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    serves_sushi = models.BooleanField(default=False)
    serves_burgers = models.BooleanField(default=False)
    serves_donats = models.BooleanField(default=False)
    serves_coffee = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.city})'

    class Meta:
        db_table = "Restaurant"
        verbose_name = "Ресторан"
        verbose_name_plural = "Ресторан"


class Waiter(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house = models.IntegerField()
    apartment = models.IntegerField()
    seniority = models.TextField()
    education = models.TextField(max_length=50)
    cources = models.TextField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = "Waiter"
        verbose_name = "Официант"
        verbose_name_plural = "Официант"


class News(models.Model):
    STATUS_CHOICES = [("on", "actively"), ("off", "not active")]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120, default="", verbose_name="название", db_index=True)
    body = models.TextField(blank=True, default="", verbose_name="содержание")
    create_date = models.DateField(auto_now_add=True, verbose_name="дата создания")
    update_date = models.DateField(auto_now=True, verbose_name="дата редактирования")
    flag_activate = models.BooleanField(default=True, verbose_name="флаг активности")
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default="off", verbose_name="Статус активности")

    def __str__(self):
        return "{} {} {}".format(
            self.title,
            self.create_date,
            self.flag_activate
        )

    def get_absolute_url(self):
        return reverse("all_news")

    class Meta:
        db_table = "News"
        ordering = ["-create_date"]
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class Comments(models.Model):
    STATUS_CHOICES = [("y", "Удалено администратором")]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, default="", verbose_name="имя пользователя", db_index=True)
    text = models.CharField(max_length=1024, default="", verbose_name="текст комментария")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=None, null=True,
                              verbose_name="Удалено администратором")
    news = models.ForeignKey("News", default=None, on_delete=models.CASCADE, null=True,
                             related_name="restaurants", verbose_name="связь с моделью новость")
    user = models.ForeignKey(Login, default=None, on_delete=models.CASCADE, null=True,
                             related_name="restaurants", verbose_name="связь с моделью пользователь")

    def __str__(self):
        return "{} {} {}".format(
            self.name,
            self.text,
            self.news
        )

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"pk": self.pk})

    @admin.display(description="текст комментария")
    def view_comment_text(self):
        return "{}...".format(self.text[:15])

    class Meta:
        db_table = "Comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий"
