from rest_framework import serializers
from .models import Category
from apps.product_sub_category.serializers import SubCategorySerializer


class CategorySerializer(serializers.ModelSerializer):
    # product_subcategory_set = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        representasion = super().to_representation(instance)
        request = self.context.get('request')
        representasion['sub_category'] = SubCategorySerializer(
            instance.product_subcategory_set,
            context={"request", request},
            many=True
        ).data
        return representasion
