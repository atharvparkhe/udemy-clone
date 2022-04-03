from django.db import models
from base.models import *


class LearnerModel(BaseUser):
    otp = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.email


class TeacherModel(BaseUser):
    otp = models.IntegerField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.email
