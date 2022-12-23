from rest_framework import serializers

from cart.models import CartItem, Cart, Purchase
from address.serializers import AddressSerializer
from authentication.serializers import UserSerializer

class PurchaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Purchase
		fields = "__all__"
	def to_representation(self, instance):
		self.fields['delivery'] = AddressSerializer(many=False, required=True)
		self.fields['client'] = UserSerializer(many=False, required=True)
		return super().to_representation(instance)

class CartSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		fields = "__all__"
	def to_representation(self, instance):
		self.fields['client'] = UserSerializer(many=False, required=True)
		return super().to_representation(instance)

class CartItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = CartItem
		fields = ['id','product','quant','value','cart']
	def to_representation(self, instance):
		self.fields['cart'] = CartSerializer(many=False, required=True)
		return super().to_representation(instance)
