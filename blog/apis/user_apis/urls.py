from django.urls import path

from .users_apis import *

app_name = 'user_apis'

urlpatterns = [
    path(
        'users/',
        UserListAPIView.as_view(),
        name='user-list'
    ),
]
