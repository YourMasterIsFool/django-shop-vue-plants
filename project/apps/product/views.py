from django.db.models.aggregates import Count, Sum
from django.db.models.expressions import ExpressionWrapper, Window
from django.db.models.fields import FloatField, IntegerField
from django.shortcuts import render
from rest_framework import viewsets
import json
from apps.product_review.serializers import ReviewSerializer
from .serializers import ProductSerializer, ProductDetailSerializer, ProductFromSerializer
from .models import Product, ProductDetail, ProductFrom
from rest_framework import permissions
from apps.product_review.models import Review, Like
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Q, F

from rest_framework.decorators import action
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    # get reviews product

    @action(detail=True)
    def reviews(self, request, pk):
        # get data review
        review = Review.objects.filter(product=pk)
        # serializing data
        review_serializer = ReviewSerializer(
            review, context={'request': request}, many=True).data
        # output reviews count for review product count
        reviews_count = review.count()
        # for ratings product with review
        ratings_avg = review.aggregate(ratings_avg=Avg('rating'))
        example = review.values('rating').distinct().annotate(
            count=Window(
                expression=Count('id'),
                partition_by=F('rating')
            )
        ).annotate(
            precentage=ExpressionWrapper(
                F('count')*100/reviews_count,
                output_field=FloatField()
            ),
        )
        print(example)
        list_rating_serializer = list(review.values('rating'))
        print(list_rating_serializer)
        context = {
            "ratings_avg": ratings_avg['ratings_avg'] if ratings_avg['ratings_avg'] else 0,
            "reviews_count": reviews_count,
            'reviews': review_serializer,
            'list_ratings': example
        }
        return Response(context, 200)


    @action(detail=False)
    def get_count(self, request):


        return Response(self.queryset.count())

    @action(detail=True)
    def details(self, request, pk):
        queryset = None
        try:
            queryset = ProductDetail.objects.get(product=pk)
            serializer = ProductDetailSerializer(
                queryset, context={'request': request})

            return Response(serializer.data, status=200)
        except ProductDetail.DoesNotExist:
            return Response(None)

    def get_queryset(self):

        query_params = self.request.query_params

        query_keywoard = query_params.get('keyword')
        print(query_keywoard)
        if(query_keywoard):
            return self.queryset.filter(Q(product_name__contains=query_keywoard))

        condition = Q()
        for key, value in query_params.items():
            condition.add(Q(**{key: value}), Q.OR)

        return self.queryset.filter(condition)

        # return super().get_queryset()

    # def get_permissions(self):
    #     if self.action in ['update', 'create', 'destroy']:
    #         self.permission_classes = [
    #             permissions.IsAdminUser, permissions.IsAuthenticated]
    #     elif self.action in ['list', 'retrieve']:
    #         self.permission_classes = [permissions.AllowAny]
    #     return super().get_permissions()


class ProductDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ProductDetailSerializer
    queryset = ProductDetail.objects.all()

    def get_queryset(self):
        query_params = self.request.query_params
        if(query_params.get('product')):
            return self.queryset.get(query_params.get('product')).first()
        return super().get_queryset()
