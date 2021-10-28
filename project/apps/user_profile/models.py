from django.db import models
from apps.user.models import User
# Create your models here.


class Profile(models.Model):
    photo = models.ImageField(upload_to="user/")
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    birth = models.DateField(null=True)
    gender = models.CharField(max_length=20, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile_set")