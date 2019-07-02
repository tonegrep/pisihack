from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from users.forms import PisiUserChangeForm, PisiUserCreationForm
from user_profile.models import PisiUser


class PisiUserAdmin(UserAdmin):
    model = PisiUser
    add_form = PisiUserCreationForm
    form = PisiUserChangeForm


admin.site.register(PisiUser, PisiUserAdmin)
