# Generated by Django 4.2.8 on 2023-12-15 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0005_alter_otp_email_alter_otp_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='otp',
            field=models.CharField(max_length=6),
        ),
    ]
