# Generated by Django 3.2.8 on 2021-10-10 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_produtrating_productrating'),
        ('favorites', '0003_alter_favorite_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
