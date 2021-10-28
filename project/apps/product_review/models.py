from django.db import models
from apps.user.models import User
from apps.product.models import Product


# Create your models here.
class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_review_set")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_review_set')


class Like(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='review_like_set')
