from rest_framework import serializers
from cart.models import CartItem, Cart, Purchase

class PurchaseSeriazlizer(serializers.ModelSerializer):
	class Meta:
		model = Purchase
		fields = "__all__"

class CartSeriazlizer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		fields = "__all__"

class CartItemSeriazlizer(serializers.ModelSerializer):
	class Meta:
		model = CartItem
		fields = "__all__"
