from rest_framework import serializers
from menu import models


class FoodImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FoodImage
        fields = ('image', )

class FoodSerializer(serializers.ModelSerializer):

    images = FoodImageSerializer(many=True)

    class Meta:
        model = models.Food
        fields = ('name', 'description','price', 'discount_price', 'images')

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