# Generated by Django 3.2.9 on 2022-01-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/images/nabin.PNG', null=True, upload_to='static/images'),
        ),
    ]