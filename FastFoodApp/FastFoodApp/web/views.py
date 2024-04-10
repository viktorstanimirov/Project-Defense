from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from FastFoodApp.products.models import Product


def index(request):
    return render(request, "common/index.html")


def menu(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "common/menu.html", context)



