from rest_framework import serializers

from blogapp.models.category_models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    Converts Category instances to and from JSON format,
    including only the 'name' field.
    """
    class Meta:
        model = Category
        field = [
            "name"
        ]