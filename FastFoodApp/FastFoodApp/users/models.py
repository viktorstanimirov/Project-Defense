from django.core.validators import MinLengthValidator
from django.db import models

from FastFoodApp.users.validators import validate_username


class User(models.Model):
    MIN_USERNAME_LENGTH = 3
    MAX_USERNAME_LENGTH = 20
    MAX_PASSWORD_LENGTH = 20

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH, message="Username must be at least 3 chars long!"),
            validate_username,
        ),
        unique=True,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        null=False,
        blank=False,
    )

