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


    def create(self, request):


        """ 
        get request user and 
        parsing into reques.data 

        """
        
        user = request.user.id
    
        request.data['user'] = user

        return super().create(request)

   
    def update(self, request, pk=None, *args, **kwargs):

        print(request.data)
        partial = kwargs.pop('partial', False)

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

