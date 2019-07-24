from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'created_at', 'updated_at']
    

    def create(self, validated_data):
        for key, value in validated_data.items():
            validated_data[key] = value.lower()
        instance, _= Category.objects.get_or_create(**validated_data)
        return instance

