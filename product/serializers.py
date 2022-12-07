from rest_framework import serializers
from .models import Product, Category, Address

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = "__all__"
