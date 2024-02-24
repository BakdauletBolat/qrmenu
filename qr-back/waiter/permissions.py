from rest_framework import permissions

from waiter.models import User, UserTypes


class IsWaiterPermission(permissions.BasePermission):
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view) -> bool:
         if request.user.is_anonymous:
             return False
         if request.user.role == UserTypes.WAITER:
             return True

         return False