from django.contrib.auth import models as auth_models
from django.contrib.auth.models import Group, Permission
from django.core.validators import MinLengthValidator
from django.db import models

from FastFoodApp.accounts.account_validators import validate_first_or_last_name_contains_only_letter, \
    validate_first_or_last_name_starts_with_capital_letter


class UserAccountCreateModel(auth_models.AbstractUser):
    FIRST_NAME_MAX_LENGTH = 25
    NAME_MIN_LENGTH = 3
    LAST_NAME_MAX_LENGTH = 30
    MAX_PHONE_NUMBER_LENGTH = 12

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(NAME_MIN_LENGTH),
            validate_first_or_last_name_contains_only_letter,
            validate_first_or_last_name_starts_with_capital_letter
        ],
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(NAME_MIN_LENGTH),
            validate_first_or_last_name_contains_only_letter,
            validate_first_or_last_name_starts_with_capital_letter,
        ],
    )

    phone_number = models.CharField(
        max_length=MAX_PHONE_NUMBER_LENGTH,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(10),

        ]
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.username}"
