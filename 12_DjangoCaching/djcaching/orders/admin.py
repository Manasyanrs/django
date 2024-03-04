from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "get_items"]

    def get_items(self, obj):
        return ", ".join([str(item.id) for item in obj.items.all()])

    get_items.short_description = 'Order'
