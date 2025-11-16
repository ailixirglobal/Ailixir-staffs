from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    path("", views.notification_list, name="list"),
    path("create/", views.create_notification, name="create"),
    path("view/<int:pk>/", views.read_notification, name="view"),
    path("read/<int:pk>/", views.mark_notification_read, name="read"),
]