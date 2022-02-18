from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'featured', views.FeaturedProductViewSet, basename='featured')
router.register(r'cart', views.CartViewSet, basename='cart')
router.register(r'wishlist', views.WishListViewSet, basename='wishlist')
router.register(r'orders', views.OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
