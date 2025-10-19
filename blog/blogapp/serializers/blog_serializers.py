from rest_framework import serializers

from blogapp.models.blog_models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "title",
            "text",
            "image",
            "created_at",
            "updated_at"
        ]