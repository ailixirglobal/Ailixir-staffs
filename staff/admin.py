from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import StaffProfile, Role


# Inline Staff Profile editing under User admin
class StaffProfileInline(admin.StackedInline):
    model = StaffProfile
    can_delete = False
    verbose_name_plural = "Staff Profile"
    fk_name = 'user'
    extra = 0


# Extend Django User Admin to include StaffProfile
class CustomUserAdmin(UserAdmin):
    inlines = (StaffProfileInline,)

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_role')
    list_select_related = ('staff_profile',)

    def get_role(self, instance):
        return instance.staff_profile.role if hasattr(instance, 'staff_profile') else "-"
    get_role.short_description = 'Role'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)


# StaffProfile standalone admin (optional but useful)
@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('user_full_name', 'role', 'department', 'phone', 'active')
    list_filter = ('role', 'department', 'active')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'role')
    ordering = ('user__first_name',)

    def user_full_name(self, obj):
        return obj.user.get_full_name()
    user_full_name.short_description = "Name"


# Unregister old User admin and register customized one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
# admin.site.register(Role)