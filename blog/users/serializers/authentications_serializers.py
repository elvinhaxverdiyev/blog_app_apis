from rest_framework import serializers
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
