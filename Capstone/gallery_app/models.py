from tkinter import CASCADE
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.fields import BooleanField, TextField
from djmoney.models.fields import MoneyField

from users_app.models import User

CATEGORY_CHOICES = (
    ('animal','ANIMAL'),
    ('music', 'MUSIC'),
    ('cinema','CINEMA'),
    ('abstract','ABSTRACT'),
    ('architecture','ARCHITECTURE'),
    ('colletibles', 'COLLECTIBLES'),
    ('utility', 'UTILITY'),
    ('photography', 'PHOTOGRAPHY'),
    ('virtual-world', 'VIRTUAL-WORLD'),
    ('various', 'VARIOUS'), 
)

def get_upload_path(instance, filename): 
    return f'images/nftimages/{filename}'

class NewGallery(models.Model):
    gallery_name = models.CharField(max_length=25)
    gallery_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='animal')
    wallett_address = models.CharField(max_length=200, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='newgallery')
    gallery_like = models.ManyToManyField(User, related_name="users", blank=True)
    public_gallery = models.BooleanField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.gallery_name

class NewNFT(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=get_upload_path)
    gallery = models.ForeignKey(NewGallery, on_delete=models.CASCADE, related_name='newnft')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usernft')
    description = models.CharField(max_length=3000, default='No description provided')
    link = models.CharField(max_length=300)
    contract_address = models.CharField(max_length=300)
    nft_created_date = models.CharField(max_length=50, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
