# Generated by Django 5.0.7 on 2024-08-27 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Erika_Admin', '0005_aboutme'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='Paragraph_1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='Erika_Bio',
            field=models.TextField(max_length=200),
        ),
    ]
