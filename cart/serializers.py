from rest_framework import serializers

from cart.models import CartItem, Cart, Purchase
from address.serializers import AddressSerializer
from authentication.serializers import UserSerializer

class PurchaseSeriazlizer(serializers.ModelSerializer):
	class Meta:
		model = Purchase
		fields = "__all__"
	def to_representation(self, instance):
		self.fields['delivery'] = AddressSerializer(many=False, required=True)
		return super().to_representation(instance)

class CartSeriazlizer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		fields = "__all__"
	def to_representation(self, instance):
		self.fields['client'] = UserSerializer(many=False, required=True)
		return super().to_representation(instance)

class CartItemSeriazlizer(serializers.ModelSerializer):
	class Meta:
		model = CartItem
		fields = ['id','product','quant','value','cart']
	def to_representation(self, instance):
		self.fields['cart'] = CartSeriazlizer(many=False, required=True)
		return super().to_representation(instance)
