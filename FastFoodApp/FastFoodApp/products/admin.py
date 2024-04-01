from django.contrib import admin

from FastFoodApp.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description", "created_at")
    list_filter = ("name", "price", "created_at")
    search_fields = ("name", "price", "description")
    ordering = ("created_at",)