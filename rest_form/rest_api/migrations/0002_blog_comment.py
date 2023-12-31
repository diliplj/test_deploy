# Generated by Django 4.2.8 on 2023-12-20 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(db_index=True, max_length=15)),
                ('title', models.CharField(max_length=50)),
                ('headline', models.TextField()),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('datamode', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Delete', 'Delete')], default='Active', max_length=257)),
            ],
            options={
                'verbose_name': 'Blog',
                'db_table': 'Blog',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('datamode', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Delete', 'Delete')], default='Active', max_length=257)),
                ('blog_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.blog')),
            ],
            options={
                'verbose_name': 'Comment',
                'db_table': 'Comment',
            },
        ),
    ]
