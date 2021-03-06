# Generated by Django 4.0 on 2022-01-25 02:58

from django.db import migrations, models
import users_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0004_remove_user_user_blog_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='images/avatars/default_image.jpg', upload_to=users_app.models.get_upload_path),
        ),
    ]
