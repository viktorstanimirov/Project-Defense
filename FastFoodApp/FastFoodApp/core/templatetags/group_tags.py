from django import template

register = template.Library()


@register.simple_tag
def calculate_total(cart_items):
    return sum(item.food_item.price * item.quantity for item in cart_items)


@register.filter(name='has_group')
def has_group(user, group_name):
    if not user.is_authenticated:
        return False
    return user.groups.filter(name=group_name).exists()
