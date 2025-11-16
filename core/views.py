from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from staff.models import StaffProfile
from django.contrib.auth.models import User

@login_required
def admin_dashboard(request):
    total_staff = StaffProfile.objects.count()
    active_staff = StaffProfile.objects.filter(active=True).count()
    roles_count = StaffProfile.objects.values('role').distinct().count()
    total_users = User.objects.count()

    context = {
        "total_staff": total_staff,
        "active_staff": active_staff,
        "roles_count": roles_count,
        "total_users": total_users,
    }
    return render(request, "dashboard/admin_dashboard.html", context)
def dashboard(request):
  return render(request, 'core/dashboard.html')
  
def add_staff(request):
  return render(request, 'core/add-member.html')