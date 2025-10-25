from django.urls import path

from .blog_apis import *

urlpatterns = [
    path(
        "blogs/",
        BlogAPIViews.as_view(),
        name="blog-list"
    ),
]
