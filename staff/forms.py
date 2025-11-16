from django import forms
from django.contrib.auth.models import User
from .models import StaffProfile
import secrets
import string


class StaffUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

    def save(self, commit=True):
        user = super().save(commit=False)

        # Generate password ONLY when user is being created
        if not user.pk:  # means user does NOT exist yet → create mode
            alphabet = string.ascii_letters + string.digits
            random_password = ''.join(secrets.choice(alphabet) for _ in range(10))

            user.set_password(random_password)
            user.generated_password = random_password  # store so view can read it
            print(random_password)
        if commit:
            user.save()

        return user

class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ['role', 'department', 'phone', 'profile_photo', 'address', 'emergency_contact', 'date_joined', 'active']