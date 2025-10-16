from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .authentication import (
    RegisterAPIView,
    LoginAPIView,
    LogOutAPIView
)

app_name = 'authentications_apis'

urlpatterns = [
    path(
        'register/',
        RegisterAPIView.as_view(),
        name='register'
    ),
    path(
        'login/',
        LoginAPIView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        LogOutAPIView.as_view(),
        name='logout'
    ),

    # # JWT endpoints
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
