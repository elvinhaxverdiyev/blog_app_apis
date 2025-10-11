from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


from users.serializers.authentications_serializers import RegisterSerializer

__all__ = [
    'RegisterAPIView'
]

class RegisterAPIView(APIView):
    """
    API View for registering a new user.
    Accepts POST requests with user data and returns a success message
    if the registration is successful, otherwise returns serializer errors.
    """
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User successfully registered"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)