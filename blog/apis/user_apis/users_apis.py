from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from users.models.user_models import CustomUser
from users.serializers.user_serializers import CustomUserSerializer


__all__ = [
    'UserListAPIView'
]

class UserListAPIView(APIView):
    http_method_names = ["get"]
    
    def get(self):
        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    