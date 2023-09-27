# primer paso para la creación de un api user
from rest_framework import serializers
from .models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# create your Serializer here

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'image',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'date_joined' ,
        ]
        # fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'is_staff',
            'is_superuser',
        ]


#  personalización de la respuesta del token con el usuario logueado
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['token'] = { 'refresh': data.pop('refresh'), 'access': data.pop('access')}
        data['user'] = UserLoginSerializer(self.user).data
        return data