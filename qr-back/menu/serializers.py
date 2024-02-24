from rest_framework import serializers
from menu import models
from waiter.models import FoodItem


class FoodImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FoodImage
        fields = ('image', )

class FoodSerializer(serializers.ModelSerializer):

    images = FoodImageSerializer(many=True)

    class Meta:
        model = models.Food
        fields = ('id','name', 'description','price', 'discount_price', 'images')

class CategorySerializer(serializers.ModelSerializer):


    foods = FoodSerializer(many=True)

    class Meta:
        model = models.Category
        fields = ('id','image', 'order', 'title', 'parent', 'foods')


class StoreSerializer(serializers.ModelSerializer):

    categories = CategorySerializer(many=True)

    class Meta:
        model = models.Store
        fields = ('name', 'address', 'image', 'categories')


class FoodItemSerializer(serializers.ModelSerializer):
    food_id = serializers.IntegerField(write_only=True, required=True)
    food = FoodSerializer(read_only=True)
    class Meta:
        model = FoodItem
        fields = ('qty', 'food', 'food_id', 'price')


