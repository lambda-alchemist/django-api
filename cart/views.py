from rest_framework import viewsets, status
from rest_framework.response import Response

from authentication.models import User
from .models import Purchase, Cart, CartItem
from .serializers import CartItemSeriazlizer, CartSeriazlizer, PurchaseSeriazlizer

class CartItemViewSet(viewsets.ModelViewSet):
	queryset = CartItem.objects.all()
	serializer_class = CartItemSeriazlizer

class CartViewSet(viewsets.ModelViewSet):
	queryset = Cart.objects.all()
	serializer_class = CartSeriazlizer
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
				status=200,
				data = CartSeriazlizer(instance, many=False))
		except:
			return Response(
				status=400,
				data={'err, try again'})

class PurchaseViewSet(viewsets.ModelViewSet):
	queryset = Purchase.objects.all()
	serializer_class = PurchaseSeriazlizer
	def create(self, request, *args, **kwargs):
		try:
			purchase = super().create(request, *args, **kwargs)
			cart = Cart.objects.get(id=purchase.data.get('content'))
			instance = Purchase.objects.get(id=purchase.data.get('id'))
			instance.price = cart.price
			instance.save()
			CartItem.objects.filter(cart = cart).delete()
			return Response(
				status=200,
				data=PurchaseSeriazlizer(instance, many=False))
		except:
			return Response(
				status=400,
				data={'err, try again'})
