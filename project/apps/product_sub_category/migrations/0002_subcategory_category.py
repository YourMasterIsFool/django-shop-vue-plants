# Generated by Django 3.2.8 on 2021-10-13 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_category', '0001_initial'),
        ('product_sub_category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='product_category.category'),
            preserve_default=False,
        ),
    ]
