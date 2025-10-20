from rest_framework import serializers

from blogapp.models.blog_images_models import BlogImagesModel


class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImagesModel
        fields = "__all__"