from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import FavoriteSerializer
from .models import Favorite


# Create your views here.
class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
