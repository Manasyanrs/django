from django.contrib.auth.models import User
from django.db import models

from shop_app.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    items = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        db_table = "Order"
        verbose_name = "order data"
        verbose_name_plural = "additional order data"
