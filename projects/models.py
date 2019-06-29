from django.db import models
from users.models import PisiUser
from model_utils.choices import Choices
from model_utils.fields import StatusField 
from django.core.validators import MaxValueValidator, MinValueValidator

COMPLETION_ZERO = 0
COMPLETION_DONE = 100


class Repository(models.Model):
    user = models.ForeignKey(PisiUser, on_delete=models.CASCADE)
    url  = models.URLField()


class Project(models.Model):
    maintainer = models.ForeignKey(PisiUser, on_delete=models.DO_NOTHING,
                                    related_name='%(class)s_project_leader')
    contributors = models.ManyToManyField(PisiUser, 
                                    related_name='%(class)s_project_participant')
    repos    = models.ManyToManyField(Repository)
    STATUS   = Choices('abandoned', 'in development', 
                        'maintained', 'on draft',
                        'complete')
    status   = StatusField()
    progress = models.IntegerField(default=0, validators=[
                                    MinValueValidator(COMPLETION_ZERO),
                                    MaxValueValidator(COMPLETION_DONE)
                                    ])



# Create your models here.
