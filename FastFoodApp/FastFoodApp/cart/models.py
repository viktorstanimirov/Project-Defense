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


class DeliveryAddress(models.Model):
    CITY_CHOICES_MAX_LENGTH = 7
    NEIGHBORHOOD_MAX_LENGTH = 40
    STREET_MAX_LENGTH = 50

    CITY_CHOICES = [
        ("Sofia", "Sofia"),
        ("Plovdiv", "Plovdiv"),
    ]
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE
    )

    city = models.CharField(
        max_length=CITY_CHOICES_MAX_LENGTH,
        choices=CITY_CHOICES,
        null=False,
        blank=False,

    )

    neighborhood = models.CharField(
        max_length=NEIGHBORHOOD_MAX_LENGTH,
        null=True,
        blank=True,

    )

    street = models.CharField(
        max_length=STREET_MAX_LENGTH,
        null=True,
        blank=True,
    )

    building_street_number = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.city}, {self.neighborhood}, {self.street}, {self.building_street_number}"




