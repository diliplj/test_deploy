# Generated by Django 4.2.8 on 2023-12-21 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_remove_blog_image_blogimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='uid',
            field=models.CharField(db_index=True, default=-111111, max_length=15),
            preserve_default=False,
        ),
    ]
