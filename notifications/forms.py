from django import forms
from .models import Notification
from staff.models import StaffProfile

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ["title", "message", "broadcast", "target_role", "target_user"]