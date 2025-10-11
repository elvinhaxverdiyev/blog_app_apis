from django.urls import path

from .authentication import *

app_name = 'authentications_apis'


urlpatterns = [
    path(
        'register/',
        RegisterAPIView.as_view(),
        name='register'
    ),
]
