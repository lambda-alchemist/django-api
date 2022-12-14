from django.db import models

from authentication.models import User
from product.models import Product
from address.models import Address

class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	quant = models.PositiveSmallIntegerField(default = 1)

	@property
	def value(self):
		return float(self.product.price * self.quant)

	def __str__(self):
		return str(self.product)

class Cart(models.Model):
	client = models.ForeignKey(User, on_delete = models.CASCADE)
	items = models.ManyToManyField(CartItem)
	price = models.FloatField(default=0.0)
	def __str__(self):
		return f'#ID {self.id}'

class Purchase(models.Model):
	delivery = models.ForeignKey(Address, on_delete = models.DO_NOTHING)
	content = models.ForeignKey(Cart, on_delete = models.DO_NOTHING)
	client = models.ForeignKey(User, on_delete = models.DO_NOTHING)
	price = models.FloatField(default = 0)
	def __str__(self):
		return f'#ID {self.id}'
