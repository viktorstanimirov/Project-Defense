from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FastFoodApp.web.urls')),
    path('products/', include('FastFoodApp.products.urls')),
    path('users/', include('FastFoodApp.users.urls')),
    path('profiles/', include('FastFoodApp.profiles.urls')),

]
