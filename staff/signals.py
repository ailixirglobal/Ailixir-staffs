from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import StaffProfile

from permissions.utils import sync_role_permissions_to_user


@receiver(post_save, sender=StaffProfile)
def update_user_permissions_based_on_role(sender, instance, **kwargs):
    sync_role_permissions_to_user(instance)
    
# @receiver(post_save, sender=User)
# def create_staff_profile(sender, instance, created, **kwargs):
#     if created:
#         StaffProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_staff_profile(sender, instance, **kwargs):
#     instance.staff_profile.save()