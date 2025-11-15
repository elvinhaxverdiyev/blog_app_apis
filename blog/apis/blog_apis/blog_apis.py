from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from blogapp.models.blog_models import Blog
from blogapp.serializers.blog_serializers import BlogSerializer
from utils.paginations import Pagination


__all__ = [
    "BlogAPIViews"
]

class BlogAPIViews(APIView):
    """
    API view to retrieve all blog posts.

    This endpoint allows anyone (no authentication required) to fetch
    the list of blog posts ordered by newest first.
    """
    permission_classes = [AllowAny]
    http_method_names = ["get"]
    
    def get(self, request):
        """
        Retrieve all blog posts.

        Returns a list of all blog entries in JSON format, ordered by descending ID
        (newest first). Uses the BlogSerializer to serialize each blog object.

        Returns:
            Response: JSON response containing serialized blog data with HTTP 200 OK.
        """
        blog = Blog.objects.all().order_by("-id") # get all blogs by id
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        