from django.db import models
import requests
from django.contrib.auth.models import AbstractUser

from allauth.socialaccount.signals import pre_social_login


class PisiUser(AbstractUser):
    pass
