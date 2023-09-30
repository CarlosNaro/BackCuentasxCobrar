from django.contrib import admin
from django.urls import path, include

#:::::::::::::: importaciones manuales ::::::::::::::
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from Apps.account.views import MyTokenObtainPairView
#::::::::::::::

urlpatterns = [
    path('admin/', admin.site.urls),
    #::: urls manuales creadas 
    path('user/', include('Apps.account.urls')),
    path('auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
