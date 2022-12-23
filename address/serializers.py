from rest_framework import serializers
from .models import Address
from authentication.serializers import UserSerializer

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = "__all__"
	# def to_representation(self, instance):
	# 	self.fields['user'] = UserSerializer(many=False, required=True)
	# 	return super().to_representation(instance)
