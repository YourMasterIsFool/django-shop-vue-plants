from django.db import models
from apps.product.models import Product

# Create your models here.


class StockIn(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='stock_in_product_set')
    quantity = models.IntegerField()
    desciption = models.TextField()

    def __str__(self):
        return f"{self.product}: {self.quantity} buah"


class StockOut(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='stock_out_product_set')
    quantity = models.IntegerField()
    desciption = models.TextField()

    def __str__(self):
        return f"{self.product}: {self.quantity} buah"
