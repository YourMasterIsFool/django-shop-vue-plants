from rest_framework import serializers
from .models import Cart
from apps.product.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        representation['product'] = ProductSerializer(
            instance.product, context={"request": request}
        ).data
        return representation

    def create(self, validated_data):


        """ update or create cart model 
            check update date when data is exist
            update the data
        """

        print(validated_data);
        cart, created = Cart.objects.update_or_create(
            product=validated_data.get('product', None),
            user=validated_data.get('user', None),

            defaults={
            'quantity': validated_data.get('quantity', None),
            'total': validated_data.get('total', None),
            'user' : validated_data.get('user')
            }
        )
        return cart




