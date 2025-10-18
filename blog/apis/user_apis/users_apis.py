from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from users.models.user_models import CustomUser
from users.serializers.user_serializers import CustomUserSerializer


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
    
    def get(self, request):
        """
        GET method:
        - Retrieves all CustomUser objects
        - Serializes them into JSON
        - Returns the data with HTTP 200 OK status
        """
        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    