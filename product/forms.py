from django import forms
from .models import Product, ProductCategory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name", "category", "description", "usage_instructions",
            "dosage", "side_effects", "storage_info",
            "price", "available", "image",
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ["name", "description"]