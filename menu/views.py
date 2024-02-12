from django.shortcuts import render
from rest_framework import decorators, response
from menu.models import Category, Food, Store
from menu.serializers import StoreSerializer


# Create your views here.


def render_shop(request, slug: str):

    store = Store.objects.get(slug=slug)
    foods = Food.objects.filter(category=store.categories.first())
    context = {
        'store': store,
        'foods': foods
    }

    return render(request, 'menu/index.html', context=context)


def render_foods_by_category(request, id: int):
    foods = Food.objects.filter(category_id=id)
    context = {
        'foods': foods
    }
    return render(request, 'menu/components/food_list.html', context=context)


@decorators.api_view(['GET'])
def render_api_store(request, slug: str):
    store = Store.objects.get(slug=slug)
    return response.Response(StoreSerializer(store, context={
        'request': request
    }).data)