from django.db.models import base
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from django.urls import path

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
# router.register(r'login', v.LoginViewSet, basename="login")
