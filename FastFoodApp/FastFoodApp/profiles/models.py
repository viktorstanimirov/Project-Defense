from django.db import models

from FastFoodApp.profiles.validators import validate_age
from FastFoodApp.users.models import User


class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 25
    MAX_LAST_NAME_LENGTH = 25
    MIN_AGE_VALUE = 18

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validate_age,
        ),
        help_text=("Age requirement: 18 years and above."
                   ),
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    users = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
