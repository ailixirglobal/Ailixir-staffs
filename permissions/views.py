from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth.models import Permission

from staff.models import StaffProfile, Role
from .models import RolePermission
from .utils import sync_role_permissions_to_user


# ============================
#   ROLE LIST
# ============================
@login_required
@permission_required("auth.view_permission", raise_exception=True)
def role_list(request):
    roles = Role.objects.all()
    return render(request, "permissions/role_list.html", {
        "roles": roles
    })


# ============================
#   EDIT ROLE PERMISSIONS
# ============================
@login_required
@permission_required("auth.change_permission", raise_exception=True)
def role_edit_permissions(request, role_id):
    role = get_object_or_404(Role, id=role_id)

    # List all Django permissions
    permissions = Permission.objects.all().order_by("content_type__app_label", "codename")

    # Permissions currently assigned to this role
    assigned = RolePermission.objects.filter(role=role).values_list("permission_id", flat=True)

    if request.method == "POST":
        selected = request.POST.getlist("permissions")

        # Remove old permissions
        RolePermission.objects.filter(role=role).delete()

        # Add new ones
        for perm_id in selected:
            RolePermission.objects.create(
                role=role,
                permission_id=perm_id
            )

        # Resync all users under this role
        staff_users = StaffProfile.objects.filter(role=role)
        for staff in staff_users:
            sync_role_permissions_to_user(staff)

        messages.success(request, "Permissions updated successfully.")
        return redirect("permissions:role_list")

    return render(request, "permissions/role_edit.html", {
        "role": role,
        "permissions": permissions,
        "assigned": assigned
    })


# ============================
#   STAFF LIST FOR ROLE ASSIGNMENT
# ============================
@login_required
@permission_required("auth.view_user", raise_exception=True)
def staff_list(request):
    staff = StaffProfile.objects.select_related("user").all()
    return render(request, "permissions/staff_list.html", {
        "staff": staff
    })


# ============================
#   ASSIGN ROLE TO STAFF
# ============================
@login_required
@permission_required("auth.change_user", raise_exception=True)
def assign_role(request, staff_id):
    staff = get_object_or_404(StaffProfile, id=staff_id)
    roles = Role.objects.all()

    if request.method == "POST":
        new_role = request.POST.get("role")

        staff.role = new_role
        staff.save()

        # Sync user permissions with new role
        sync_role_permissions_to_user(staff)

        messages.success(request, "Role updated successfully.")
        return redirect("permissions:staff_list")

    return render(request, "permissions/assign_role.html", {
        "staff": staff,
        "roles": roles
    })