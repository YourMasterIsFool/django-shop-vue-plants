from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductDetailViewSet
from django.urls import path, include


router = DefaultRouter()

router.register(r'products', ProductViewSet, basename="product")
router.register(r'product-detail', ProductDetailViewSet,
                basename="product-detail")
# router.register(r'categories', CategoryViewSet, basename="category")


urlpatterns = [

]

urlpatterns += router.urls
