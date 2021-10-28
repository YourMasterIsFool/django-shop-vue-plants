from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()

router.register(r'stock-in', StockInViewSet, basename="stock-in")
router.register(r'stock-out', StockOutViewSet, basename="stock-out")
