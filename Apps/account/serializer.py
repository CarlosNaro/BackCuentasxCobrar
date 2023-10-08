# primer paso para la creación de un api user
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# create your Serializer here
class UserDjangoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UserLoginSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = "__all__"
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'username':instance.username,
            'is_admin':instance.profile.is_admin,
        }

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