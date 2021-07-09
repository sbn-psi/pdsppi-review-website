from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['pk', 'email', 'username', 'first_name', 'last_name']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'display_name', 'addtl_info', 'photo',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('display_name', 'addtl_info', 'photo',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)