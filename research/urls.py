from django.urls import path
from . import views

app_name = "research"

urlpatterns = [
    path("experiments/", views.experiment_list, name="experiment_list"),
    path("experiments/add/", views.experiment_add, name="experiment_add"),
    path("experiments/<int:exp_id>/", views.experiment_detail, name="experiment_detail"),
    path("labnotes/", views.labnote_list, name="labnote_list"),
    path("labnotes/<int:exp_id>/add/", views.labnote_add, name="labnote_add"),
]