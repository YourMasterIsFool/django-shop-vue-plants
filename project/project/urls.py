"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


# router import rest_framework
from rest_framework.routers import DefaultRouter
from apps.product.urls import router as product_router
from apps.user.urls import router as user_router
from apps.favorites.urls import router as favorites_router
from apps.cart.urls import router as cart_router
from apps.product_category.urls import router as product_category_router
from apps.product_stock.urls import router as product_stock_router
from apps.product_review.urls import router as product_review_router


# router for web service
router = DefaultRouter()
router.registry.extend(product_router.registry)
router.registry.extend(user_router.registry)
router.registry.extend(favorites_router.registry)
router.registry.extend(cart_router.registry)
router.registry.extend(product_category_router.registry)
router.registry.extend(product_stock_router.registry)
router.registry.extend(product_review_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),

    # api
    path('api/', include([
        path('', include(router.urls)),

        # djoser
        path('auth/', include('djoser.urls')),

        # djoser authenticate json web tokne
        path('auth/', include('djoser.urls.jwt')),

    ])),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
