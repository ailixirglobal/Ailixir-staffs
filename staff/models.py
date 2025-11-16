from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
  ROLE_CHOICES = [
        ('management', 'Management'),
        ('production', 'Production'),
        ('research', 'Research & Development'),
        ('quality', 'Quality Control'),
        ('sales', 'Sales & Marketing'),
        ('customer', 'Customer Support'),
        ('logistics', 'Logistics'),
        ('admin', 'Administrative Staff'),
    ]
  name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)
  
  def __str__(self):
    return self.get_name_display()
class StaffProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    profile_photo = models.FileField(upload_to='staff/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    date_joined = models.DateField()

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['user__last_name', 'user__first_name']

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.role})"