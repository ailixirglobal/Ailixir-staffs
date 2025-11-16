from django.contrib.auth.models import Permission
from staff.models import StaffProfile
from .models import RolePermission


def sync_role_permissions_to_user(staff_profile):
    """
    Syncs the user's permissions with the current role assigned in StaffProfile.

    - Clears all old permissions
    - Adds all permissions linked to the current role
    - Ensures the user's permission set always matches their active role
    """

    user = staff_profile.user

    # Defensive checks
    if not user or not staff_profile.role:
        return

    # Clear all previous role-based permissions
    user.user_permissions.clear()

    # Get all permissions linked to this role
    perm_ids = RolePermission.objects.filter(
        role__name=staff_profile.role.name
    ).values_list("permission_id", flat=True)

    # Assign them to the user
    if perm_ids:
        user.user_permissions.set(perm_ids)
    # Save changes
    user.save()