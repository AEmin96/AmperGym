from django.db import models
from django.contrib.auth.models import User
import os
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    newsletter = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

