# Generated by Django 2.0.3 on 2018-04-03 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='Bangladesh', max_length=70),
        ),
    ]
