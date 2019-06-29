from django.db import models

from pisihack import settings
from user_profile.models import UserProfile
from users.models import PisiUser
from model_utils.choices import Choices
from model_utils.fields import StatusField
from django.core.validators import MaxValueValidator, MinValueValidator

COMPLETION_ZERO = 0
COMPLETION_DONE = 100


class Repository(models.Model):
    repo_id = models.IntegerField()

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=3092)

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                               default='')


class Project(models.Model):
    maintainer = models.ForeignKey(UserProfile,
                                   on_delete=models.DO_NOTHING,
                                   related_name='%(class)s_project_leader')
    contributors = models.ManyToManyField(UserProfile,
                                          related_name='%(class)s_project_participant')
    repos = models.ManyToManyField(Repository)
    STATUS = Choices('abandoned', 'in development',
                     'maintained', 'on draft',
                     'complete')
    status = StatusField()
    progress = models.IntegerField(default=0, validators=[
        MinValueValidator(COMPLETION_ZERO),
        MaxValueValidator(COMPLETION_DONE)
    ])
    vacant_slots = models.IntegerField(default=0, validators=[
                            MinValueValidator(0),
                            MaxValueValidator(128)
                        ])


# Create your models here.
