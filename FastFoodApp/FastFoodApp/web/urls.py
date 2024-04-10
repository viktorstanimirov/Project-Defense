from django.contrib.auth import admin
from django.urls import path

from FastFoodApp.web.views import index, menu

urlpatterns = (
    path('', index, name='index'),
    path('menu/', menu, name='menu'),
)
