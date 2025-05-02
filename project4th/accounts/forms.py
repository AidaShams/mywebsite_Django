from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserRegistration

class CustomUserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUserRegistration
        fields = UserCreationForm.Meta.fields + ('age',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUserRegistration
        fields = UserChangeForm.Meta.fields