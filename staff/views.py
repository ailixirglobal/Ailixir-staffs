from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import StaffProfile
from .forms import StaffUserForm, StaffProfileForm

@login_required
def view_profile(request, staff_id=None):
    # If staff_id is provided, admin is viewing another staff profile
    if staff_id:
        profile = get_object_or_404(StaffProfile, id=staff_id)
    else:
        # Otherwise, user is viewing their own profile
        profile = request.user.staff_profile

    return render(request, "staff/view_staff.html", {
        "profile": profile
    })

@login_required
def staff_list(request):
    staffs = StaffProfile.objects.select_related("user").all()
    return render(request, "staff/staff_list.html", {"staffs": staffs})


@login_required
def staff_add(request):
    if request.method == "POST":
        user_form = StaffUserForm(request.POST)
        profile_form = StaffProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("staff:list")
    else:
        user_form = StaffUserForm()
        profile_form = StaffProfileForm()

    return render(request, "staff/staff_add.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })


@login_required
def staff_detail(request, pk):
    staff = get_object_or_404(StaffProfile, pk=pk)
    return render(request, "staff/staff_detail.html", {"staff": staff})


@login_required
def staff_edit(request, pk):
    staff = get_object_or_404(StaffProfile, pk=pk)
    user = staff.user

    if request.method == "POST":
        user_form = StaffUserForm(request.POST, instance=user)
        profile_form = StaffProfileForm(request.POST, request.FILES, instance=staff)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("staff:list")
    else:
        user_form = StaffUserForm(instance=user)
        profile_form = StaffProfileForm(instance=staff)

    return render(request, "staff/staff_edit.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "staff": staff
    })