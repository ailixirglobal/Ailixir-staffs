from django.urls import path
from . import views

app_name = "permissions"

urlpatterns = [
    path("roles/", views.role_list, name="role_list"),
    path("roles/<int:role_id>/edit/", views.role_edit_permissions, name="role_edit"),

    path("staff/", views.staff_list, name="staff_list"),
    path("staff/<int:staff_id>/assign/", views.assign_role, name="assign_role"),
]