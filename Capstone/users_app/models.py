from distutils.command.upload import upload
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.fields import BooleanField, TextField

def get_upload_path(instance, filename):
    return f'images/avatars/{filename}'

class User(AbstractUser):

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    avatar = models.ImageField(upload_to=get_upload_path, default='images/avatars/nftexample.png')

    def __str__(self):
        return self.username

