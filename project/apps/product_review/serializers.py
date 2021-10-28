from rest_framework import serializers
from .models import Review, Like
from apps.user.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    def get_user(self, obj):
        user = UserSerializer(obj.user).data
        data = {
            "name": user['name'],
            "id": user['id']
        }
        return data

    def get_likes(self, obj):
        return obj.review_like_set.count()

    class Meta:
        model = Review
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = "__all__"
