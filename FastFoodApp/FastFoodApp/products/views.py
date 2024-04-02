from django.urls import reverse_lazy
from django.views import generic as view

from FastFoodApp.products.forms import ProductCreateForm
from FastFoodApp.products.models import Product


class ProductCreateView(view.CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "products/create-food.html"

    def get_success_url(self):
        return reverse_lazy("menu")
