from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers.authentications_serializers import RegisterSerializer
from users.serializers.authentications_serializers import LoginSerializer

__all__ = [
    'RegisterAPIView',
    'LoginAPIView',
    'LogOutAPIView'
]

class RegisterAPIView(APIView):
    """
    API View for registering a new user.
    Accepts POST requests with user data and returns a success message
    if the registration is successful, otherwise returns serializer errors.
    """
    permission_classes = [AllowAny]
    http_method_names = ["post"]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User successfully registered"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class LoginAPIView(APIView):
    """
    Handles user login requests.

    Accepts POST with credentials and returns JWT tokens on success.
    """
    permission_classes = [AllowAny]
    http_method_names = ["post"]

    def post(self, request):
        """Validate user credentials and return tokens if valid."""
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LogOutAPIView(APIView):
    """
    Logs out an authenticated user by blacklisting their refresh token.

    POST request expects a 'refresh' token in the request data.
    Returns 205 on success, 400 if token is invalid, or error if missing.
    """
    permission_classes = [IsAuthenticated]
    http_method_names = ["post"]
    def post(self, request):
        refresh_token = request.data.get('refresh')
        
        if not refresh_token:
            return Response({"error": "token is required"})
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)