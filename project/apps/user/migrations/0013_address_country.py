# Generated by Django 3.2.8 on 2021-10-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20211006_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]