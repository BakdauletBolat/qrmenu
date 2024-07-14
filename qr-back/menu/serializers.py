from rest_framework import serializers
from menu import models
from waiter.models import FoodItem


class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodImage
        fields = ('image',)


class FoodCategorySerializer(serializers.Serializer):
    title = serializers.CharField()
    id = serializers.IntegerField()


class FoodSerializer(serializers.ModelSerializer):
    images = FoodImageSerializer(many=True)
    category = FoodCategorySerializer()
    class Meta:
        model = models.Food
        fields = ('id', 'name', 'description', 'price', 'discount_price', 'images', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'image', 'order', 'title', 'parent')


class StoreSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    class Meta:
        model = models.Store
        fields = ('name', 'address', 'image', 'categories', 'params')


class FoodItemSerializer(serializers.ModelSerializer):
    food_id = serializers.IntegerField(write_only=True, required=True)
    food = FoodSerializer(read_only=True)

    class Meta:
        model = FoodItem
        fields = ('qty', 'food', 'food_id', 'price')
