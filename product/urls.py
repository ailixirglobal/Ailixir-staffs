from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list, name="list"),
    path("add/", views.product_add, name="add"),
    path("category/add/", views.category_add, name="category_add"),
    path("<slug:slug>/", views.product_detail, name="detail"),
    path("<slug:slug>/edit/", views.product_edit, name="edit"),
]