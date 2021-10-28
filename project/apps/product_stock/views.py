from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StockInSerializer
from .models import StockIn, StockOut


# Create your views here.
class StockInViewSet(viewsets.ModelViewSet):
    serializer_class = StockInSerializer
    queryset = StockIn.objects.all()


class StockOutViewSet(viewsets.ModelViewSet):
    serializer_class = StockInSerializer
    queryset = StockOut.objects.all()
