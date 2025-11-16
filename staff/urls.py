from django.urls import path
from . import views

app_name = "staff"

urlpatterns = [
    path("", views.staff_list, name="list"),
    path("add/", views.staff_add, name="add"),
    path("<int:pk>/", views.staff_detail, name="detail"),
    path("<int:pk>/edit/", views.staff_edit, name="edit"),
    path("profile/", views.view_profile, name="my_profile"),
    path("profile/<int:staff_id>/", views.view_profile, name="profile"),
]