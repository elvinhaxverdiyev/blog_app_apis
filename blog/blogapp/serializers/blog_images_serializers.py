from rest_framework import serializers

from blogapp.models.blog_images_models import BlogImagesModel


class BlogImageSerializer(serializers.ModelSerializer):
    """
    Serializer for BlogImagesModel.
    Provides serialization and deserialization of blog image data,
    including all model fields.
    """
    class Meta:
        model = BlogImagesModel
        fields = "__all__"