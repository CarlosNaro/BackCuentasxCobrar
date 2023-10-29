from django.shortcuts import render

from .serializer import MyTokenObtainPairSerializer
from rest_framework import  status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Profile
from django.contrib.auth.models import User
from .serializer import ProfileSerializer, UserDjangoSerializer

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getUserByID(request):
    try:
        profile = Profile.objects.get(id=request.user.id)
        user  = User.objects.get(id=request.user.id)
        profile_serializer = ProfileSerializer(profile)
        user_serializer = UserDjangoSerializer(user)
        return Response({'profile':profile_serializer.data,'user_django':user_serializer.data})
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)