# Generated by Django 3.2.8 on 2021-10-06 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
