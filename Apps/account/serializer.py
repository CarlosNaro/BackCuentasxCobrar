# primer paso para la creación de un api user
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# create your Serializer here
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UserDjangoSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = "__all__"
    
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'is_staff':instance.profile.is_admin,
            'username':instance.username,
        }

class LoginUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ["id" ,"username", "is_staff"]
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'username':instance.username,
            'is_staff':instance.is_staff,
        }

#Customizing the token response 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['token'] = { 
            'refresh': data.pop('refresh'), 
            'access': data.pop('access')
            }
        data['user'] = LoginUserSerializer(self.user).data
        return data   