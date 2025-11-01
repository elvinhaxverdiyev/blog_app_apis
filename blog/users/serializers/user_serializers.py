from rest_framework import serializers

from users.models.user_models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for the CustomUser model."""
    class Meta:
        model = CustomUser
        fields = "__all__"
        
        
        
 