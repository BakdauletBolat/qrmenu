from django.db import models
from django.contrib.auth.models import AbstractUser
from menu import models as menu_models
from menu.models import Store


class UserTypes(models.TextChoices):
    ADMIN = "ADMIN", "Админ"
    WAITER = "WAITER", "Официант"


class User(AbstractUser):
    role = models.CharField(choices=UserTypes, max_length=12)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='users', null=True)

class WaiterTable(models.Model):
    table = models.PositiveIntegerField(null=True, blank=True)
    user_uuid = models.UUIDField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    waiter = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def total_cost(self):
        cost = 0
        for item in self.food_items.all():
            cost += item.price * item.qty
        return cost


class FoodItem(models.Model):
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    food = models.ForeignKey(menu_models.Food, on_delete=models.CASCADE, related_name='food_items')
    table = models.ForeignKey(WaiterTable, on_delete=models.CASCADE, related_name='food_items')