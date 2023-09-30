# primer paso para la creación de un api user
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# create your Serializer here
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'is_staff',
        ]

#  personalización de la respuesta del token con el usuario logueado
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['token'] = { 
            'refresh': data.pop('refresh'), 
            'access': data.pop('access')
            }
        data['user'] = UserLoginSerializer(self.user).data
        return data