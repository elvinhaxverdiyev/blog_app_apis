from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .authentication import RegisterAPIView

app_name = 'authentications_apis'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),

    # JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
