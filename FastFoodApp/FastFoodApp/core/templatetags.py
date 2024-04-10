from django import template

register = template.Library()


@register.simple_tag
def calculate_total(cart_items):
    return sum(item.food_item.price * item.quantity for item in cart_items)
