from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Profile
from .serializers import ProfileSerializer
# Create your views here.



class ProfileViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
	serializer_class = ProductSerializer
	queryset = Profile.objects.all()

	def retrieve(self, request, pk=None):
