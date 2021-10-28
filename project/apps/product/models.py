from django.db import models
from apps.product_sub_category.models import SubCategory
from apps.product_category.models import Category
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to="products/")
    product_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="published")

    def __str__(self):

        return self.product_name


class ProductFrom(models.Model):
    product_from = models.CharField(max_length=100)

    def __str__(self):
        return self.product_from


class ProductDetail(models.Model):
    weight = models.IntegerField()
    description = models.TextField()
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name='product_detail_set')
    product_from = models.ForeignKey(
        ProductFrom, on_delete=models.DO_NOTHING, related_name='product_from_set')

    def __str__(self):

        return f"{self.product} {self.weight}"
