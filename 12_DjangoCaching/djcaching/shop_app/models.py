from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=25, null=False, blank=True)
    description = models.TextField(null=True, blank=True, max_length=255)
    price = models.FloatField(null=False, default=0, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}"

    def get_absolute_url(self):
        return reverse("home_page")

    class Meta:
        db_table = "Product"
        verbose_name = "product"
        verbose_name_plural = "product"
