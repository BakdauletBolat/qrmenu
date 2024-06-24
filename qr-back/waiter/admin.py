from typing import Any
from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from waiter import models
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import gettext_lazy as _


class UserAdmin(DefaultUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password", "role")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

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


# @admin.register(models.WaiterTable)
class WaiterTable(admin.ModelAdmin):
    inlines = [FoodItemTabularAdmin]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(waiter__store_id=request.user.store_id)
