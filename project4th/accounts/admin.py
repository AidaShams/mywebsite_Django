from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserRegistration
from .forms import CustomUserChangeForm, CustomUserChangeForm
# Register your models here.
class ShowAdminPage(UserAdmin):
    list_display = ['username', 'is_staff', 'age']
    form = CustomUserChangeForm
    model = CustomUserRegistration
    add_form = CustomUserRegistration
    fieldsets = (
        (None, {'fields':('username','password',)}),
        ('Personal info', {'fields':('first_name','last_name','email','age',)}),
        ('Permissions', {'fields':('is_staff','is_active','is_superuser','groups','user_permissions')}),
        ('Important dates', {'fields':('last_login','date_joined')}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('username','age','password1','password2',)
        })
    )

admin.site.register(CustomUserRegistration, ShowAdminPage)