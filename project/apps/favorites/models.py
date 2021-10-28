from django.db import models

from apps.user.models import User
from apps.product.models import Product

# Create your models here.


class Favorite(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
