from django.urls import path

from apis.user_apis import *


urlpatterns = [
    path(
        "users/",
        UserListAPIView.as_view(),
        name="user-list"
    ),
]

