from rest_framework import serializers
from .models import User
from apps.user_profile.serializers import ProfileSerializer


class UserSerializer(serializers.ModelSerializer):

    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        representation['profile'] = None
        if instance.user_profile_set != None:
            representation['profile'] = ProfileSerializer(
            instance.user_profile_set, context={"request": request}).data 
        return representation

        
    class Meta:
        model = User
        fields = ('email', 'id',  'is_staff')
        write_only_fields = ('password',)
