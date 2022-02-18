from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter

from .models import Category, Product
from users.models import WishList, Cart, Order
from .serializers import CategorySerializer, ProductSerializer, WishListSerializer, CartSerializer, OrderSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ('name',)
    lookup_field = 'name'


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ('name', 'description', 'category__name')
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ('category',)


class FeaturedProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows featured products to be viewed or edited.
    """
    queryset = Product.objects.filter(is_featured=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class WishListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows wish lists to be viewed or edited.
    """
    def get_queryset(self):
        return WishList.objects.filter(user=self.request.user)

    serializer_class = WishListSerializer
    permission_classes = [permissions.IsAuthenticated]


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows carts to be viewed or edited.
    """
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

