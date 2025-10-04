from rest_framework import serializers

from users.models.user_image_model import UsersImageModel


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersImageModel
        fields = "__all__"
        