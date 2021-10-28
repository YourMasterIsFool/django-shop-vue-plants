from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, LikeViewSet

router = DefaultRouter()

router.register(r'reviews', ReviewViewSet, basename='product-review')
router.register(r'reviews-like', LikeViewSet, basename='product-review-like')
