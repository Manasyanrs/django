from django.contrib import admin
from .models import News, Comments, Waiter, Restaurant


class ViewEditCommentNews(admin.TabularInline):
    model = Comments


class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "create_date", "flag_activate", "status"]
    list_filter = ["flag_activate"]
    list_editable = ["flag_activate"]
    inlines = [ViewEditCommentNews]
    actions = ["transfer_to_active", "transfer_to_not_active"]

    def transfer_to_active(self, request, queryset):
        queryset.update(status="on")

    def transfer_to_not_active(self, request, queryset):
        queryset.update(status="off")

    transfer_to_active.short_description = "Перевод в статус активно"
    transfer_to_not_active.short_description = "Перевод в статус не активно"


class CommentsAdmin(admin.ModelAdmin):
    list_display = ["name", "view_comment_text", "status"]
    list_filter = ["name"]
    actions = ["removed_by_admin"]

    def removed_by_admin(self, request, queryset):
        queryset.update(status="y")

    removed_by_admin.short_description = "Удалить?"


class WaiterAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age", "sex"]
    fieldsets = (
        ("Данные работника", {
            "fields": ("first_name", "last_name", "age", "sex")
        }),
        ("Адрес проживания", {
            "fields": ("country", "city", "street", "house", "apartment")
        }),
        ("Дополнительные сведения", {
            "fields": ("restaurant", "seniority", "education", "cources")
        })
    )


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "country", "city", "street", "chef"]
    fieldsets = (
        ("Информация о ресторане", {
            "fields": ("name", "description")
        }),
        ("Сотрудники", {
            "fields": ("count_of_employers", "director", "chef")
        }),
        ("Адрес ресторана", {
            "fields": ("country", "city", "street", "house", "phone")
        }),
        ("Услуги ресторана", {
            "fields": ("serves_hot_dogs", "serves_pizza", "serves_sushi",
                       "serves_burgers", "serves_donats", "serves_coffee")
        })
    )


admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Waiter, WaiterAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
