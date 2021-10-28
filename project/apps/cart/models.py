from django.db import models
from apps.product.models import Product
from apps.user.models import User


# Create your models here.


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
