from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from users.models.user_models import CustomUser
from users.serializers.user_serializers import CustomUserSerializer
from utils.paginations import Pagination


__all__ = [
    'UserListAPIView'
]


class UserListAPIView(APIView):
    """
    API View to list all registered users.
    Accepts only GET requests.
    """
    permission_classes = [AllowAny]
    http_method_names = ["get"]
    pagination_class = Pagination
    
    def get(self, request):
        """
        GET method:
        - Retrieves all CustomUser objects
        - Serializes them into JSON
        - Returns the data with HTTP 200 OK status
        """
        user = CustomUser.objects.all().order_by("-id") #get all user and orderinf by id
        paginator = self.pagination_class()  #call paginator class fir paginated users 
        paginated_users = paginator.paginate_queryset(user, request, view=self)
        
        serializer = CustomUserSerializer(paginated_users, many=True)
        return paginator.get_paginated_response(serializer.data) #return paginated user
    