from decimal import Context
from functools import partial
from rest_framework import serializers
from .models import Favorite

# product serializer
from apps.product.serializers import ProductSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        representation['product'] = ProductSerializer(
            instance.product, context={"request": request}).data

        return representation

    class Meta:
        model = Favorite
        fields = "__all__"
