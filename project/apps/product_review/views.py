from django.shortcuts import render
from rest_framework.response import Response
from django.db.models import Avg
from .serializers import ReviewSerializer, LikeSerializer
from .models import Like, Review
from rest_framework import viewsets

# Create your views here.


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
