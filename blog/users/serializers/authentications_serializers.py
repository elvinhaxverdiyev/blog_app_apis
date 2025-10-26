from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password

from users.models.user_models import CustomUser
from users.models.user_image_model import UsersImageModel
from utils.validations import check_password_length


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Handles password validation, optional profile image upload, 
    and user creation with related image model.
    """
    password = serializers.CharField(required=True, write_only=True, min_length=6)
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password", "username", "name", "bio", "image"]
        
    def validate_password(self, value):
        """Validate password using Django validators and custom length check."""
        validate_password(value)
        if not check_password_length(value):
            raise serializers.ValidationError("Password must be between 4 and 10 characters.")
        return value

    def create(self, validated_data):
        """Create a new user and save profile image if provided."""
        image = validated_data.pop("image", None)
        password = validated_data.pop("password")
        email = validated_data.pop("email")  

        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            **validated_data  
        )

        if image:
            UsersImageModel.objects.create(user=user, image=image)

        return user



class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    Authenticates user and returns JWT tokens with basic user info.
    """
    email = serializers.EmailField()
    password = serializers.CharField(required=True, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    def get_user(self, obj):
        user = obj.get('user')
        if not user:
            return None
        return {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "name": user.name,
        }

    def validate(self, attrs):
        email = attrs.get("email").strip()
        password = attrs.get("password").strip()

        if not email or not password:
            raise serializers.ValidationError("Email və parol daxil edilməlidir")

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Email və ya parol yanlışdır")
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        return {
            "refresh": str(refresh),
            "access": str(access),
            "user": {
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "name": user.name
            }
        }