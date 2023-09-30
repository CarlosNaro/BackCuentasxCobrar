# tercer paso para la creación de un api user
from django.db import router
from rest_framework.routers import DefaultRouter
from .viewSets import UserViewSet

# create routers

router = DefaultRouter()
router.register('user',UserViewSet)