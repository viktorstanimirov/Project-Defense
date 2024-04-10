from django.urls import path

from FastFoodApp.cart.views import add_to_cart, cart_details, update_cart

urlpatterns = (
    path("cart_details", cart_details, name="cart_details"),
    path("add_to_cart/<int:pk>", add_to_cart, name="add_to_cart"),
    path('update-cart/<int:item_id>/<str:action>/', update_cart, name='update_cart'),
)