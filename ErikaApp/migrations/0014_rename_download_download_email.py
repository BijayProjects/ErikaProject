# Generated by Django 5.0.7 on 2024-09-04 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ErikaApp', '0013_download'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Download',
            new_name='Download_email',
        ),
    ]