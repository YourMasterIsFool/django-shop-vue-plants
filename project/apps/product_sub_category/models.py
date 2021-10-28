from django.db import models
from apps.product_category.models import Category
# Create your models here.


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name='product_subcategory_set')
    sub_category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.sub_category}"
