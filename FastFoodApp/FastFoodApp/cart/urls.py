from django.urls import path

from FastFoodApp.cart.views import add_to_cart, cart_details, update_cart, confirm_order, DeliveryAddressView

urlpatterns = (
    path("cart_details", cart_details, name="cart_details"),
    path("confirm_order", confirm_order, name="confirm_order"),
    path("delivery_address", DeliveryAddressView.as_view(), name="delivery_address"),
    path("add_to_cart/<int:pk>", add_to_cart, name="add_to_cart"),
    path('update-cart/<int:item_id>/<str:action>/', update_cart, name='update_cart'),
)