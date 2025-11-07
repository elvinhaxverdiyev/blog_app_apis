from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #admin url
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
    path(
        'api/v1/',
        include('apis.blog_apis.urls')
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)