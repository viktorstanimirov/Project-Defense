from django.core.paginator import Paginator
from django.shortcuts import render

from FastFoodApp.products.models import Product


def index(request):
    return render(request, "common/index.html")


# def menu(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, "common/menu.html", context)
#


def menu(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 6)  # Show 10 products per page.

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    page_obj = paginator.get_page(page_number)

    context = {'products': products, 'page_obj': page_obj}
    return render(request, "common/menu.html", context)
