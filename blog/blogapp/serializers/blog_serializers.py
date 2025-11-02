from rest_framework import serializers

from blogapp.models.blog_models import Blog


class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for the Blog model.
    Handles conversion between Blog instances and JSON representations,
    including title, text, image, created_at, and updated_at fields.
    """
    class Meta:
        model = Blog
        fields = [
            "title",
            "text",
            "image",
            "created_at",
            "updated_at"
        ]