from django.urls import path

from FastFoodApp.products.views import ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = (
    path("create-food/", ProductCreateView.as_view(), name="create-food"),
    path("details-food/<int:pk>/", ProductDetailView.as_view(), name="details-food"),
    path("update-food/<int:pk>/", ProductUpdateView.as_view(), name="update-food"),
    path("delete-food/<int:pk>/", ProductDeleteView.as_view(), name="delete-food"),
)