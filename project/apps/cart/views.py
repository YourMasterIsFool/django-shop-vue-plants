from django.db.models import query
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import request, serializers, viewsets
from .models import Cart
from .serializers import CartSerializer
from rest_framework import permissions
from rest_framework.response import Response

# Create your views here.


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user)
        return queryset



