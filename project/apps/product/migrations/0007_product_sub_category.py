# Generated by Django 3.2.8 on 2021-10-13 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_sub_category', '0003_alter_subcategory_category'),
        ('product', '0006_auto_20211012_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_sub_category.subcategory'),
        ),
    ]
