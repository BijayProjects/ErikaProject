# Generated by Django 5.0.7 on 2024-08-18 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Erika_Admin', '0003_receive_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receive_contact',
            old_name='email',
            new_name='Email',
        ),
    ]