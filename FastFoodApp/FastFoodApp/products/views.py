from django.urls import reverse_lazy
from django.views import generic as view

from FastFoodApp.products.forms import ProductCreateForm, ProductUpdateForm, ProductDeleteForm
from FastFoodApp.products.models import Product


class ProductCreateView(view.CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "products/create-food.html"

    def get_success_url(self):
        return reverse_lazy("menu")


class ProductDetailView(view.DetailView):
    model = Product
    template_name = "products/details-food.html"
    context_object_name = "product"


class ProductUpdateView(view.UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = "products/update-food.html"

    def get_success_url(self):
        return reverse_lazy("menu")


class ProductDeleteView(view.DeleteView):
    model = Product
    template_name = "products/delete-food.html"
    success_url = reverse_lazy("menu")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProductDeleteForm(initial=self.object.__dict__)

        return context
