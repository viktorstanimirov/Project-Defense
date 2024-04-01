from django.db import models


class Product(models.Model):
    MAX_NAME_LENGTH = 50
    PRICE_MAX_DIGITS = 5
    PRICE_DECIMAL_PLACES = 2

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )
    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES,
        null=False,
        blank=False,
    )
    description = models.TextField()

    image = models.ImageField(
        upload_to="images/",
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name
