from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# Create your models here.

class CustomUser (AbstractUser):
    display_name  = models.CharField(verbose_name=_("Display name"), max_length=30, help_text=_("Will be shown e.g. when commenting"), default=(""))
    addtl_info    = models.CharField(verbose_name=_("Additional information"), max_length=4096, blank=True, null=True)
    photo         = models.ImageField(verbose_name=_("Photo"), upload_to='photos/', default='photos/default-user-avatar.png')

    class Meta:
        ordering = ['last_name']

    def get_absolute_url(self):
        return reverse('account_profile')

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"

