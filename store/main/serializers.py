from rest_framework import serializers
from main.models import Product, Category, SubCategory, Item


class ProductSerializer(serializers.ModelSerializer):
    class Meta:

        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = SubCategory
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:

        model = Item
        fields = '__all__'

