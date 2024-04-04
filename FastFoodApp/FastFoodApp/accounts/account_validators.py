from django.core.exceptions import ValidationError


def validate_first_or_last_name_contains_only_letter(value):
    if not value.isalpha():
        raise ValidationError("First name must contain only alphabetic characters.")


def validate_first_or_last_name_starts_with_capital_letter(value):
    if not value[0].isupper():
        raise ValidationError("First name must start with a capital letter.")
