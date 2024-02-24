from rest_framework import serializers

from menu.serializers import FoodItemSerializer
from waiter import models


class TableCreateSerializer(serializers.ModelSerializer):

    food_items = FoodItemSerializer(many=True)
    user_uuid = serializers.UUIDField(required=True)
    table = serializers.CharField(required=False)
    total_cost = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.WaiterTable
        fields = ('id', 'table','is_active', 'user_uuid', 'food_items','waiter','total_cost')


class AssignTableSerializer(serializers.Serializer):
    id = serializers.CharField()
    table = serializers.CharField()

class UpdateTableSerializer(serializers.Serializer):
    id = serializers.CharField()
    status = serializers.BooleanField()