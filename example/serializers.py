from rest_framework import serializers
from .models import Category, ProductHistory


class ProductSerializer(serializers.ModelSerializer):  # sus
    class Meta:
        model = ProductHistory
        fields = ('id', 'price', 'date', 'category_id')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'link', 'shop')
