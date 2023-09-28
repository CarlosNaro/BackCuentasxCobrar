# segundo paso para la creación de un api user
from .models import User
from .serializer import UserSerializer
from rest_framework.viewsets import ModelViewSet



# create your ViewSets here

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
