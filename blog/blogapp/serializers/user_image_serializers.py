from rest_framework import serializers

from blogapp.models.user_image_models import UsersImageModel


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersImageModel
        fields = "__all__"
        