# Generated by Django 4.2.8 on 2023-12-21 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0005_blog_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogimages',
            name='uid',
        ),
    ]
