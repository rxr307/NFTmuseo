# Generated by Django 4.0 on 2022-02-14 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0010_alter_newgallery_gallery_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newgallery',
            name='gallery_name',
            field=models.CharField(max_length=25),
        ),
    ]