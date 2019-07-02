from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from pisihack import settings

# class Profile(models.Model):
#     user = models.ForeignKey(PisiUser, on_delete=models.DO_NOTHING)


MAX_POINTS = 505000
MIN_POINTS = 0
MAX_LEVEL = 100
MIN_LEVEL = 0


class PisiUser(AbstractUser):
    total_points = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(MAX_POINTS),
                    MinValueValidator(MIN_POINTS)]
    )


# ex: backend, system programming etc.
class Subject(models.Model):
    user = models.ForeignKey(PisiUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.URLField()
    lvl = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(MAX_LEVEL),
                    MinValueValidator(MIN_LEVEL)]
    )
    # def calculate_level(self):
    #     lvl = MIN_LEVEL
    #     point = MIN_POINTS
    #     skills = Skill.objects.filter(subject = self)
    #     for skill in skills:
    #         lvl += skill.lvl
    #         point += skill.point 
    #         if point >= MAX_POINTS:
    #             lvl+=1
    #             point-=MAX_POINTS
    #     self.lvl = lvl
    #     self.point = point


# ex: LLVM, SystemC, Vue.js etc.
class Skill(models.Model):
    user = models.ForeignKey(PisiUser, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.URLField()
    exp = models.IntegerField(default=0,
                              validators=[MaxValueValidator(MAX_POINTS),
                                          MinValueValidator(MIN_POINTS)]
                              )

    def get_lvl(self):
        exp = self.exp
        cap = 100
        counter = 0
        while exp > 0:
            exp - cap
            cap += 100
            counter += 1
        return counter


