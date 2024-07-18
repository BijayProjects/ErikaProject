# Generated by Django 5.0 on 2024-06-20 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_intro', models.TextField()),
                ('blog_body', models.TextField()),
                ('image', models.ImageField(upload_to='Blog_media')),
            ],
        ),
    ]
