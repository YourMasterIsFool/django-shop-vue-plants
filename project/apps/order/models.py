from django.db import models
from apps.user.models import User
from apps.product.models import Product
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
