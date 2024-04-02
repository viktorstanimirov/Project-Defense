from django.urls import path

from FastFoodApp.products.views import ProductCreateView

urlpatterns = (
    path("create-food/", ProductCreateView.as_view(), name="create-food"),
)