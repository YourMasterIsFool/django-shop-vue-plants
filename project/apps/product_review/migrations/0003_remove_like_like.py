# Generated by Django 3.2.8 on 2021-10-16 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_review', '0002_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='like',
        ),
    ]
