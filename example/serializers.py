from rest_framework import serializers
from .models import Category, PhoneHistory, LaptopHistory, KeyboardHistory, MonitorHistory, Phone

# class PriceSerializer(serializers.ModelSerializer): # для цен
#     price = serializers.SlugRelatedField(slug_field='price', read_only=True)
#     shop_id = serializers.SlugRelatedField(slug_field='title', read_only=True)
#
#     class Meta:
#         model = Price
#         fields = ('price','shop_id')
#
# class ItemListSerializer(serializers.ModelSerializer): # для листов товаров
#     category = serializers.SlugRelatedField(slug_field='title', read_only=True)
#
#     def get_price(self, obj):
#         try:
#             price = serializers.SlugRelatedField(slug_field='price', read_only=True, many=True)
#             # price = obj.
#             serializer = PriceSerializer(price)
#             return serializer.data
#         except Exception as ex:
#             return None
#
#
#     class Meta:
#         model = Item
#         fields = ('id','title','price', 'category')


# class ProductSerializer(serializers.ModelSerializer):
#     def get_price(self, obj):
#         try:
#             price = serializers.SlugRelatedField(slug_field='price', read_only=True, many=True)
#             serializer = PhoneSerializer(price)
#             return serializer.data
#         except Exception as ex:
#             return None
#
#     class Meta:
#         model = Category
#         fields = ('id', 'title', 'link', 'shop', 'price')


class PhoneFullSerializer (serializers.ModelSerializer):
    prices = serializers.StringRelatedField(many=True)

    class Meta:
        model = Phone
        fields = ['id', 'title', 'link', 'prices']


class PhoneSerializer(serializers.ModelSerializer):  # sus
    class Meta:
        model = PhoneHistory
        fields = ('id', 'price', 'date', 'category_id')


class LaptopSerializer(serializers.ModelSerializer):  # sus
    class Meta:
        model = LaptopHistory
        fields = ('id', 'price', 'date', 'category_id')


class KeyboardSerializer(serializers.ModelSerializer):  # sus
    class Meta:
        model = KeyboardHistory
        fields = ('id', 'price', 'date', 'category_id')


class MonitorSerializer(serializers.ModelSerializer):  # sus
    class Meta:
        model = MonitorHistory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'link', 'shop')
