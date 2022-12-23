from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from .models import Purchase, Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer, PurchaseSerializer

class CartItemViewSet(viewsets.ModelViewSet):
	queryset = CartItem.objects.all()
	serializer_class = CartItemSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return CartItem.objects.filter(cart_id = self.request.user.pk)

class CartViewSet(viewsets.ModelViewSet):
	queryset = Cart.objects.all()
	serializer_class = CartSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Cart.objects.filter(client_id = self.request.user.pk)

	def create(self, request, *args, **kwargs):
		try:
			final_value = 0
			cart = super().create(request, *args, **kwargs)
			items = CartItem.objects.filter(id__in=cart.data.get('items'))
			for item in items:
				final_value += item.value
			instance = Cart.objects.get(id=cart.data.get('id'))
			instance.price = final_value
			instance.save()
			return Response(
				status=status.HTTP_201_CREATED,
				data=CartSerializer(instance, many=False))
		except:
			return Response(
				status=status.HTTP_400_BAD_REQUEST,
				data={'err, try again'})

class PurchaseViewSet(viewsets.ModelViewSet):
	queryset = Purchase.objects.all()
	serializer_class = PurchaseSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Purchase.objects.filter(client_id = self.request.user.pk)

	def create(self, request, *args, **kwargs):
		try:
			purchase = super().create(request, *args, **kwargs)
			cart = Cart.objects.get(id=purchase.data.get('content'))
			instance = Purchase.objects.get(id=purchase.data.get('id'))
			instance.price = cart.price
			instance.save()
			CartItem.objects.filter(cart_id = cart.pk).delete()
			return Response(
				status=status.HTTP_201_CREATED,
				data=PurchaseSerializer(instance, many=False))
		except:
			return Response(
				status=status.HTTP_400_BAD_REQUEST,
				data={'err, try again'})
