from django.core.exceptions import ValidationError


def validate_age(age):
    if age < 18:
        raise ValidationError("Age must be 18 or above!")