# Generated by Django 3.2.8 on 2021-10-17 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_review', '0011_rename_user_review_user_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user_review',
            new_name='user',
        ),
    ]
