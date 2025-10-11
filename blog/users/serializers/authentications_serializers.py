from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from users.models.user_models import CustomUser
from users.models.user_image_model import UsersImageModel


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password", "username", "name", "bio", "image"]

    def create(self, validated_data):
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
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
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
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise serializers.ValidationError("Email və parol daxil edilməlidir")

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Email və ya parol yanlışdır")

        # Token yaradılır
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        # JSON serializable dict qaytarılır
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