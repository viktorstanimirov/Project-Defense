from celery import shared_task
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic as view
from django.views.decorators.http import require_POST

from FastFoodApp.cart.forms import DeliveryAddressForm
from FastFoodApp.cart.models import Cart, CartItem, DeliveryAddress
from FastFoodApp.products.models import Product

UserModel = get_user_model()


@require_POST
def add_to_cart(request, pk):
    app_user = get_object_or_404(UserModel, id=request.user.id)
    cart, created = Cart.objects.get_or_create(user=app_user)

    food_item = get_object_or_404(Product, id=pk)

    item, created = CartItem.objects.get_or_create(cart=cart, food_item=food_item)

    if created:
        pass
    else:
        item.quantity += 1
        item.save()

    return redirect("menu")


# @shared_task
# def remove_cart_items(cart_item_id):
#     Cart.objects.filter(id=cart_item_id, expired=True).delete()


def remove_shoping_cart_item(item_id):
    try:
        item = CartItem.objects.get(id=item_id)
        item.delete()
    except CartItem.DoesNotExist:
        pass


@login_required
def cart_details(request):
    try:
        cart = Cart.objects.get(user=request.user, )
        cart_items = cart.items.all()
        total_price = sum(item.food_item.price * item.quantity for item in cart_items)

    except Cart.DoesNotExist:
        cart = None
        cart_items = []
        total_price = sum(item.food_item.price * item.quantity for item in cart_items)

    context = {
        "cart": cart,
        "cart_items": cart_items,
        "total_price": total_price,
    }
    return render(request, "cart/cart_details.html", context)


def update_cart(request, item_id, action):
    cart = Cart.objects.get(user=request.user)

    if action == "add":
        cart_item = cart.items.get(id=item_id)
        cart_item.quantity += 1
        cart_item.save()
    elif action == "remove":
        cart_item = cart.items.get(id=item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    elif action == "delete":
        cart_item = cart.items.get(id=item_id)
        cart_item.delete()

    return redirect("cart_details")


def confirm_order(request):
    context = {
        "UserModel": UserModel
    }
    if not UserModel.first_name or not UserModel.last_name or not UserModel.email:
        return redirect("profile", context)
    return render(request, "cart/confirm_order.html", context)


class DeliveryAddressView(view.CreateView):
    model = DeliveryAddress
    form_class = DeliveryAddressForm
    template_name = "cart/delivery_address.html"

    def form_valid(self, form):
        obj, created = DeliveryAddress.objects.update_or_create(
            user=self.request.user,
            defaults={
                'city': form.cleaned_data['city'],
                'neighborhood': form.cleaned_data['neighborhood'],
                'street': form.cleaned_data['street'],
                'building_street_number': form.cleaned_data['building_street_number'],
            }
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('confirm_order')
