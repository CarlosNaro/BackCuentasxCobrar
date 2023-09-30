# cuarto paso para la creación de un api user
from .routers import * #verificar acción
from django.urls import path, include
from .viewSets import UserViewSet
from .views import getUserByID

# Create your urls here.
urlpatterns = [
    path('',include(router.urls)),
    path('getUserByID/',getUserByID),
]