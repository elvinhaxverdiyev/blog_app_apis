from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from blogapp.models.blog_models import Blog
from blogapp.serializers.blog_serializers import BlogSerializer
from utils.paginations import Pagination


class BlogAPIViews(APIView):
    
    def get(self, request):
        blog = Blog.objects.all().order_by("-id")
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        