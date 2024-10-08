# Generated by Django 5.0 on 2024-07-11 09:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ErikaApp', '0003_email_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
