# Generated by Django 3.2.9 on 2022-01-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20220107_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(default='static/images/bg1.jpg', upload_to='images/'),
        ),
    ]
