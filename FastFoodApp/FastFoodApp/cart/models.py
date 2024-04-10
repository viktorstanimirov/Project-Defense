from django.contrib.auth import get_user_model
from django.db import models

from FastFoodApp.products.models import Product

UserModel = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name='items',
        on_delete=models.CASCADE
    )
    food_item = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        default=1
    )

    def get_cost(self):
        return self.food_item.price * self.quantity

    def __str__(self):
        return f"{self.food_item.name} - Quantity: {self.quantity} - Cost: {self.get_cost()}"
