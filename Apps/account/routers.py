# tercer paso para la creación de un api user
from django.db import router
from rest_framework.routers import DefaultRouter
from .viewSets import ProfileViewSet , UserViewSet

# create routers

router = DefaultRouter()
router.register('profile',ProfileViewSet)
router.register('user',UserViewSet)