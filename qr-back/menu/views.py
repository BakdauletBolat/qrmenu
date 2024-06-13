from rest_framework import decorators, response
from menu.models import Category, Food, Store
from menu.serializers import StoreSerializer, FoodSerializer, CategorySerializer


@decorators.api_view(['GET'])
def get_store(request, slug: str):
    store = Store.objects.get(slug=slug)
    return response.Response(StoreSerializer(store, context={
        'request': request
    }).data)


@decorators.api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    return response.Response(CategorySerializer(categories, context={
        'request': request
    }).data)


@decorators.api_view(['GET'])
def get_foods_by_category(request, id: int):
    foods = Category.objects.get(id=id).foods
    return response.Response(FoodSerializer(foods,many=True, context={
        'request': request
    }).data)


@decorators.api_view(['GET'])
def get_detail_food(request, id: int):
    product = Food.objects.get(id=id)
    return response.Response(FoodSerializer(product, context={
        'request': request
    }).data)

