# Generated by Django 3.2.8 on 2021-10-24 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(default='published', max_length=20),
        ),
    ]
