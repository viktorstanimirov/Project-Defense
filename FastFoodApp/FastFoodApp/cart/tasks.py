from celery import shared_task

from FastFoodApp.cart.models import Cart


@shared_task
def remove_cart_items(cart_item_id):
    Cart.objects.filter(id=cart_item_id, expired=True).delete()
