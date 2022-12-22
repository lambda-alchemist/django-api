from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"
	def to_representation(self, instance):
		self.fields['category'] = CategorySerializer(many=False, required=True)
		return super().to_representation(instance)

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = "__all__"


