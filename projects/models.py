from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.choices import Choices
from model_utils.fields import StatusField

from user_profile.models import PisiUser

COMPLETION_ZERO = 0
COMPLETION_DONE = 100


class Repository(models.Model):
    repo_id = models.IntegerField()

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=3092)

    author = models.ForeignKey(PisiUser, on_delete=models.CASCADE,
                               default='')

    last_updated = models.DateTimeField(default=datetime.min)

    def __str__(self):
        return self.name


class Project(models.Model):
    maintainer = models.ForeignKey(PisiUser,
                                   on_delete=models.DO_NOTHING,
                                   related_name='%(class)s_project_leader')
    contributors = models.ManyToManyField(PisiUser,
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
    vacant_slots = models.IntegerField(
        default=0, validators=[
            MinValueValidator(0),
            MaxValueValidator(128)
        ])

    VISIBILITY_CHOICES = (
        (1, _("Public")),
        (2, _("Private")),
    )

    visibility = models.SmallIntegerField(
        choices=VISIBILITY_CHOICES, default=1)

# Create your models here.
