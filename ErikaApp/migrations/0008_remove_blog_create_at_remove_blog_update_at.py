# Generated by Django 5.0 on 2024-07-11 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ErikaApp', '0007_remove_blog_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='update_at',
        ),
    ]
