from rest_framework import viewsets, status
from rest_framework.response import Response

from authentication.models import User
from .models import Purchase, Cart, CartItem
from .serializers import CartItemSeriazlizer, CartSeriazlizer, PurchaseSeriazlizer

class PurchaseViewSet(viewsets.ModelViewSet):
	queryset = Purchase.objects.all()
	serializer_class = PurchaseSeriazlizer

class CartItemViewSet(viewsets.ModelViewSet):
	queryset = CartItem.objects.all()
	serializer_class = CartItemSeriazlizer

class CartViewSet(viewsets.ModelViewSet):
	queryset = Cart.objects.all()
	serializer_class = CartSeriazlizer

	def create(self, request, *args, **kwargs):
		import pdb; pdb.set_trace()
		try:
			final_val = 0
			items = CartItem.objects.filter(id__in = [request.data.get('items')])
			for loop in items:
				final_val += loop.product.price
			cart = super().create(request, *args, **kwargs)
			instance = Cart.objects.get(id = cart.data.get('id'))
			instance.val = final_val
			instance.save()
			return Response(CartSeriazlizer(cart, many = False ).data, status = status.HTTP_200_OK)
		except:
			return Response(data={'err, try again'}, status = status.HTTP_400_BAD_REQUEST)
