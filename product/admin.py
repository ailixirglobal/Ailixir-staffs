from django.contrib import admin
from .models import Product, ProductCategory

@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "available", "created_at")
    list_filter = ("category", "available")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}