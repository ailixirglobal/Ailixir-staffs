from django.db import models
from django.contrib.auth.models import User
from staff.models import StaffProfile

class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sent_notifications")
    title = models.CharField(max_length=200)
    message = models.TextField()

    # Targeting options
    broadcast = models.BooleanField(default=False)
    target_role = models.CharField(max_length=50, blank=True, null=True)
    target_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="direct_notifications")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    class Meta:
        permissions = [
            ("can_create_notification", "Can create notification"),
        ]


class NotificationRead(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.notification.title}"