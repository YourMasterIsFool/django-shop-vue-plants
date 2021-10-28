from django.db import models
from apps.user.models import User

# Create your models here.


class Address(models.Model):
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_address_set")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} addreess "
