# Generated by Django 3.2.8 on 2021-10-10 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_produtrating_productrating'),
        ('favorites', '0002_remove_favorite_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]