from django.contrib.auth import models as auth_models
from django.contrib.auth.models import Group, Permission
from django.core.validators import MinLengthValidator
from django.db import models

from FastFoodApp.accounts.account_validators import validate_first_or_last_name_contains_only_letter, \
    validate_first_or_last_name_starts_with_capital_letter


class AppUser(auth_models.AbstractUser):
    FIRST_NAME_MAX_LENGTH = 25
    NAME_MIN_LENGTH = 3
    LAST_NAME_MAX_LENGTH = 30
    MAX_PHONE_NUMBER_LENGTH = 12

    email = models.EmailField(unique=True)

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(NAME_MIN_LENGTH),
            validate_first_or_last_name_contains_only_letter,
            validate_first_or_last_name_starts_with_capital_letter,
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
        validators=[MinLengthValidator(10)],
    )

    date_of_birth = models.DateField(null=True, blank=True)

    profile_picture = models.ImageField(
        upload_to="media/profile_pictures/",
        default="media/profile_pictures/profile_picture.png",
        blank=True,
        null=True
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name="appuser_set",
        related_query_name="appuser",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name="appuser_set",
        related_query_name="appuser",
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.username}"


