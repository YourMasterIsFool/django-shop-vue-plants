from django.db import models
from django.db.models.aggregates import Avg, Sum
from rest_framework import serializers
from .models import Product, ProductDetail, ProductFrom
from apps.product_sub_category.serializers import SubCategorySerializer
import math

class ProductFromSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFrom
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    product_from = ProductFromSerializer()


    class Meta:
        model = ProductDetail
        fields = ("description", 
                  "weight", "product", "product_from")


class ProductSerializer(serializers.ModelSerializer):

    stock = serializers.SerializerMethodField(read_only=True)
    ratings_avg = serializers.SerializerMethodField(read_only=True)
    product_detail = ProductDetailSerializer(
        source="product_detail_set", read_only=True)
    reviews_count = serializers.SerializerMethodField(read_only=True)

    def get_stock(self, obj):

        stock_in = obj.stock_in_product_set.aggregate(
            total=Sum('quantity')).get('total') or 0
        stock_out = obj.stock_out_product_set.aggregate(
            total=Sum('quantity')).get('total') or 0

        # stock = stock_in - stock_out
        return stock_in - stock_out


    def get_ratings_avg(self, obj):

        ratings = obj.product_review_set.aggregate(
            total=Sum('rating')
        ).get('total') or 5

        return math.ceil(ratings)

    def get_reviews_count(self, obj):
        count = obj.product_review_set.count()

        return count
  
    class Meta:
        model = Product
        fields = ['id', 'product_name', 
                    'reviews_count',
                    'ratings_avg',
                    'category',
                    'status',
                    'date',
                  'product_price', 'stock', 'product_detail',  'product_image']
