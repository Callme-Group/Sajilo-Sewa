# Generated by Django 3.2.9 on 2022-01-08 09:31

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='about.jpg', null=True, upload_to=homepage.models.profile_pic_directory),
        ),
    ]
