from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


class FeedBack(models.Model):
    fb_field = models.TextField(max_length=1000)

    def __str__(self):
        return self.fb_field
