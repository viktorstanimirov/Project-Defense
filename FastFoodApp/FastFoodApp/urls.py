from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FastFoodApp.web.urls')),
    path('products/', include('FastFoodApp.products.urls')),
    path('accounts/', include('FastFoodApp.accounts.urls')),
    path('cart/', include('FastFoodApp.cart.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
