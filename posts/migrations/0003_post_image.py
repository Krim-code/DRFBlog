# Generated by Django 5.0.6 on 2024-05-10 12:44

import posts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=posts.models.get_image_filename),
        ),
    ]
