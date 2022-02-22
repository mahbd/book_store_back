from rest_framework import serializers

from .models import Category, Product
from users.models import WishList, Cart, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    is_wish_listed = serializers.SerializerMethodField()
    is_in_cart = serializers.SerializerMethodField()

    def get_is_wish_listed(self, obj):
        request = self.context['request']
        if not request.user.is_authenticated:
            return False
        return WishList.objects.filter(user=request.user, item=obj).exists()

    def get_is_in_cart(self, obj):
        request = self.context['request']
        if not request.user.is_authenticated:
            return False
        return Cart.objects.filter(user=request.user, item=obj).exists()

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'image', 'stock', 'category', 'is_featured', 'created_at',
                  'is_wish_listed', 'is_in_cart')


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('id', 'user', 'item')

    def validate(self, data):
        user = self.context['request'].user
        data['user'] = user
        return data


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'item', 'quantity')

    def validate(self, data):
        user = self.context['request'].user
        data['user'] = user
        return data


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'item', 'quantity', 'total_price', 'status', 'created_at')

    def validate(self, data):
        user = self.context['request'].user
        data['user'] = user
        return data
