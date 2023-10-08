







from .routers import *
from django.urls import path, include
from .viewSets import ProductViewSet

urlpatterns = [
    path('',include(router.urls)),
]