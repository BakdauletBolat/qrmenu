from typing import Any

from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from waiter import models

class UserAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj):
        if request.user.is_superuser:
            fields = ('role',('username', 'password'),'store', 'email', 'first_name', 'last_name', 'groups', 'last_login', 'is_superuser', 'is_staff')
        else:
            fields = ('role','username', 'password', 'email', 'first_name', 'last_name')
        return fields

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(store_id=request.user.store_id)


admin.site.register(models.User, UserAdmin)


class FoodItemTabularAdmin(admin.TabularInline):
    model = models.FoodItem
    can_delete = False

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(models.WaiterTable)
class WaiterTable(admin.ModelAdmin):
    inlines = [FoodItemTabularAdmin]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(waiter__store_id=request.user.store_id)


