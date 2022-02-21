from django.contrib import admin

from .models import User, WishList, Cart, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active', 'is_superuser')
    list_display_links = ('id', 'username')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'email')
    list_per_page = 25


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item')
    list_display_links = ('id', 'user')
    list_filter = ('user',)
    search_fields = ('user', 'item')
    list_per_page = 25


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item', 'quantity')
    list_display_links = ('id', 'user')
    list_filter = ('user',)
    search_fields = ('user', 'item')
    list_per_page = 25


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item', 'quantity', 'total_price', 'status', 'created_at')
    list_display_links = ('id', 'user', 'item')
    list_filter = ('user',)
    search_fields = ('user', 'item')
    list_per_page = 25
