from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "category", "location", "quantity", "status")
    search_fields = ("name", "sku", "category")
    list_filter = ("status", "category", "location")
