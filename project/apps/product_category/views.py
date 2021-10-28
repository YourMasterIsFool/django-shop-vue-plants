from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category
from rest_framework import permissions
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.AllowAny,)
