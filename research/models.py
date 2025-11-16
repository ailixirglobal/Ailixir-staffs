from django.db import models
from django.contrib.auth.models import User


class Experiment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    lead_researcher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="lead_experiments")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("paused", "Paused"),
    ])

    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.title


class LabNote(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, related_name="notes")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    note = models.TextField()
    attachment = models.FileField(upload_to="research/notes/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        

    def __str__(self):
        return f"{self.experiment.title} - {self.title}"