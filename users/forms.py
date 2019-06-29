# users/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PisiUser


class PisiUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = PisiUser
        fields = ('username', 'email')


class PisiUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = PisiUser
        fields = UserChangeForm.Meta.fields
