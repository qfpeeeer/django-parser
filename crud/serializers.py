from rest_framework import serializers
from models.models import Product


class ProductFullSerializer(serializers.ModelSerializer):
    prices = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'title', 'link', 'prices']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'title', 'link']