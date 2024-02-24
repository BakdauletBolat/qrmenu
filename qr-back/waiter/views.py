from django.db import transaction
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import decorators, exceptions
from waiter.models import WaiterTable, FoodItem
from waiter.serializers import AssignTableSerializer, TableCreateSerializer, UpdateTableSerializer
from rest_framework.permissions import IsAuthenticated

from waiter.permissions import IsWaiterPermission

@decorators.api_view(['GET'])
@decorators.permission_classes([IsAuthenticated, IsWaiterPermission])
def waiter_table_list(request):
    tables = WaiterTable.objects.filter(waiter_id=request.user.id)
    return Response(TableCreateSerializer(tables, many=True).data)


@decorators.api_view(['GET'])
@decorators.permission_classes([IsAuthenticated, IsWaiterPermission])
def waiter_table_detail(request, id: int):
    table = WaiterTable.objects.get(id=id)
    return Response(TableCreateSerializer(table).data)


@decorators.api_view(['POST'])
@transaction.atomic
def create_table_from_user(request):
    serializer = TableCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    current_table = WaiterTable.objects.filter(user_uuid=serializer.validated_data.get('user_uuid'), is_active=True).first()
    food_items = serializer.validated_data.pop('food_items')
    if current_table:
        current_table.food_items.all().delete()
        FoodItem.objects.bulk_create([FoodItem(**food_item, table_id=current_table.id) for food_item in food_items])
        return Response({
            'id': current_table.id
        })
    else:
        new_table = WaiterTable.objects.create(**serializer.validated_data)
        FoodItem.objects.bulk_create([FoodItem(**food_item, table_id=new_table.id) for food_item in food_items])
        return Response({
            'id': new_table.id
        })


@decorators.api_view(['POST'])
@decorators.permission_classes([IsAuthenticated, IsWaiterPermission])
@transaction.atomic
def assign_to_waiter(request):
    serializer = AssignTableSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    table = WaiterTable.objects.get(id=serializer.validated_data.get('id'))
    table.waiter_id = request.user.id
    table.table = serializer.validated_data.get('table')
    table.save()
    return Response({
        'id': table.id
    })


@decorators.api_view(['get'])
@decorators.permission_classes([IsAuthenticated, IsWaiterPermission])
def check_assign(request, pk):
    table = WaiterTable.objects.get(id=pk)
    if table.table or table.waiter_id:
        raise exceptions.APIException('TABLE_TAKE')
    return Response({}, status=200)


@decorators.api_view(['post'])
@decorators.permission_classes([IsAuthenticated, IsWaiterPermission])
def update_table_status(request):
    serializer = UpdateTableSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    table = WaiterTable.objects.get(id=serializer.validated_data.get('id'))
    table.is_active = serializer.validated_data.get('status')
    table.save()
    return Response({
        'id': table.id
    })
