from rest_framework import serializers

from blogapp.models.category_models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = [
            "name"
        ]