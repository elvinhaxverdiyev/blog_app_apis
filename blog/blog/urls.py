from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'api/v1/',
        include('apis.authentication_apis.urls')
    ),
    path(
        'api/v1/',
        include('apis.user_apis.urls')
    ),
]
