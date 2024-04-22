from django.urls import path

from FastFoodApp.web.views import index, menu, custom_404

urlpatterns = (
    path('', index, name='index'),
    path('menu/', menu, name='menu'),
)

handler404 = 'FastFoodApp.web.views.custom_404'
