# Generated by Django 5.0.7 on 2024-08-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Erika_Admin', '0004_rename_email_receive_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Signature', models.CharField(max_length=50)),
                ('Erika_Bio', models.CharField(max_length=200)),
                ('Paragraph', models.TextField(help_text='For the Better view, You can user <br> when ever you want break point in your paragraph.')),
                ('Author_Image', models.ImageField(upload_to='Media')),
            ],
        ),
    ]
