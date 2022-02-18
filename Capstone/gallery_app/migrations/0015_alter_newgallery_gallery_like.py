# Generated by Django 4.0 on 2022-02-18 17:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery_app', '0014_delete_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newgallery',
            name='gallery_like',
            field=models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]