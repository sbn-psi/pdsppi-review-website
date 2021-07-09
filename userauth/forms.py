from django import forms
from .models import CustomUser
from wagtail.users.forms import UserCreationForm, UserEditForm
from django.forms import ModelForm

class WagtailUserCreationForm(UserCreationForm):
    class  Meta(UserCreationForm.Meta):
        model = CustomUser


class WagtailUserEditForm(UserEditForm):
    class Meta(UserEditForm.Meta):
        model  = CustomUser

class CustomUserUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'display_name', 'addtl_info', 'photo',]

        