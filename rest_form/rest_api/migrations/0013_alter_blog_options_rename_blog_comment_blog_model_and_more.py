# Generated by Django 4.2.8 on 2023-12-19 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0012_rename_article_blog_alter_blog_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='blog',
            new_name='blog_model',
        ),
        migrations.AlterModelTable(
            name='blog',
            table='Blog',
        ),
    ]