from django.db import models

from authentication.models import User
from product.models import Product
from address.models import Address


class Cart(models.Model):
	client = models.ForeignKey(User, on_delete = models.CASCADE)
	price = models.FloatField(default=0.0)
	def __str__(self):
		return f'#ID {self.pk}'

class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	quant = models.PositiveSmallIntegerField(default = 1)
	cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING, related_name='cartitem_set')
	@property
	def value(self):
		return float(self.product.price * self.quant)
	def __str__(self):
		return f'#ID {self.pk}'

class Purchase(models.Model):
	delivery = models.ForeignKey(Address, on_delete = models.DO_NOTHING)
	content = models.ForeignKey(Cart, on_delete = models.DO_NOTHING)
	client = models.ForeignKey(User, on_delete = models.DO_NOTHING)
	price = models.FloatField(default = 0)
	def __str__(self):
		return f'#ID {self.pk}'
