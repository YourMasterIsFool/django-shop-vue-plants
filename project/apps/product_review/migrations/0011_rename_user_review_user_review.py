# Generated by Django 3.2.8 on 2021-10-17 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_review', '0010_alter_review_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='user_review',
        ),
    ]
