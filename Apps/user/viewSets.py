# segundo paso para la creación de un api user
from .models import User
from .serializer import UserSerializer, MyTokenObtainPairSerializer
from rest_framework.viewsets import ModelViewSet



# create your ViewSets here

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#  creación de un api Login con JWT que devuelve un token y el usuario logueado

