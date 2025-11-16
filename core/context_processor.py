from .menus import ROLE_MENUS
from notifications.models import NotificationRead, Notification

def general_context(request):
  if not request.user.is_authenticated:
        return {}
  unread_count = NotificationRead.objects.filter(user=request.user, read=False).count()
  latest_notifications = NotificationRead.objects.filter(user=request.user).select_related("notification")[:10]
  
  return {
    "latest_notifications": latest_notifications,
    'unread_count' : unread_count,
  }

def role_based_menu(request):
    if not request.user.is_authenticated:
        return {}

    profile = getattr(request.user, "staff_profile", None)
    if not profile:
        return {}

    role = profile.role
    menu = ROLE_MENUS.get(role.name, [])

    return {
        "role_menu": menu
    }