from django.urls import path

from FastFoodApp.web.views import index

urlpatterns = (
    path('', index, name='index'),
)