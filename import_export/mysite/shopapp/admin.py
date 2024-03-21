import json
from http import HTTPStatus

from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import path

from .models import Product, Order, ProductImage
from .admin_mixins import ExportAsCSVMixin
from .forms import OrderForm


class OrderInline(admin.TabularInline):
    model = Product.orders.through


class ProductInline(admin.StackedInline):
    model = ProductImage


@admin.action(description="Archive products")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description="Unarchive products")
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
    ]
    inlines = [
        OrderInline,
        ProductInline,
    ]
    # list_display = "pk", "name", "description", "price", "discount"
    list_display = "pk", "name", "description_short", "price", "discount", "archived"
    list_display_links = "pk", "name"
    ordering = "-name", "pk"
    search_fields = "name", "description"
    fieldsets = [
        (None, {
            "fields": ("name", "description"),
        }),
        ("Price options", {
            "fields": ("price", "discount"),
            "classes": ("wide", "collapse"),
        }),
        ("Images", {
            "fields": ("preview",),
        }),
        ("Extra options", {
            "fields": ("archived",),
            "classes": ("collapse",),
            "description": "Extra options. Field 'archived' is for soft delete",
        })
    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."


# admin.site.register(Product, ProductAdmin)


# class ProductInline(admin.TabularInline):
class ProductInline(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    change_list_template = "shopapp/orders_changelist.html"
    inlines = [
        ProductInline,
    ]
    list_display = "delivery_address", "promocode", "created_at", "user_verbose"

    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")

    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username

    def import_csv(self, request: HttpRequest) -> HttpResponse:
        if request.method == "GET":
            form = OrderForm()
            context = {"form": form}
            return render(request, "admin/csv_form.html", context)
        form = OrderForm(request.POST, request.FILES)
        if not form.is_valid():
            context = {"form": form}
            return render(request, "admin/csv_form.html", context, status=HTTPStatus.BAD_REQUEST)

        json_file = form.cleaned_data["json_order"]
        data = json.load(json_file)
        for order in data:
            order_data = order.get("fields")
            order_data["user"] = User.objects.get(
                pk=order_data.get("user")
            )
            product_ids = order_data.pop("products")

            new_order = Order.objects.create(**order_data)
            new_order.products.set(product_ids)
            new_order.save()

        self.message_user(request, "Data from JSON imported.")
        return redirect("..")

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("upload-json-order/", self.import_csv, name="upload-json"),
        ]

        return custom_urls + urls
