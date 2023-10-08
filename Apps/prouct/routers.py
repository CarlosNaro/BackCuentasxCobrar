





from django.db import router
from rest_framework.routers import DefaultRouter
from .viewSets import ProductViewSet

router = DefaultRouter()
router.register('product',ProductViewSet)