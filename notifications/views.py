from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from .forms import NotificationForm
from .models import Notification, NotificationRead
from staff.models import StaffProfile
from django.utils import timezone


@login_required
def read_notification(request, pk):
    notif = get_object_or_404(NotificationRead, pk=pk, user=request.user)

    # Mark as read if not already
    if not notif.read:
        notif.read = True
        notif.read_at = timezone.now()
        notif.save()

    context = {
        "notif": notif,
    }
    return render(request, "notifications/read.html", context)

@login_required
@permission_required('notifications.add_notification', raise_exception=True)
def create_notification(request):
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            notif = form.save(commit=False)
            notif.sender = request.user
            notif.save()

            # Determine recipients
            if notif.broadcast:
                recipients = User.objects.all()
            elif notif.target_role:
                recipients = [
                    s.user for s in StaffProfile.objects.filter(role=notif.target_role)
                ]
            else:
                recipients = [notif.target_user]

            # Create unread statuses
            for user in recipients:
                NotificationRead.objects.create(notification=notif, user=user)

            return redirect("notifications:list")
    else:
        form = NotificationForm()

    return render(request, "notifications/create.html", {"form": form})


@login_required
def notification_list(request):
    notifs = NotificationRead.objects.filter(user=request.user).select_related("notification")
    return render(request, "notifications/list.html", {"notifications": notifs})


@login_required
def mark_notification_read(request, pk):
    notif = NotificationRead.objects.get(id=pk, user=request.user)
    notif.read = True
    notif.read_at = timezone.now()
    notif.save()
    return redirect("notifications:list")