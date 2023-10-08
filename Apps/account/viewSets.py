# segundo paso para la creación de un api user
from .models import Profile
from .serializer import ProfileSerializer, UserDjangoSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

# create your ViewSets here
class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDjangoSerializer