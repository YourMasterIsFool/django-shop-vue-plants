from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.decorators import action

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        user = get_object_or_404(self.queryset, pk=request.user.id)
        serializer = self.get_serializer(user)

        return Response(serializer.data)

    
        


class LoginViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
