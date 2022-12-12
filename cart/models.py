from itertools import product
from django.db import models

from authentication.models import User
from product.models import Product
from address.models import Address

class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	client = models.ForeignKey(User, on_delete = models.CASCADE)
	quant = models.PositiveSmallIntegerField(default = 1)

	@property
	def value(self):
		return float(self.product.price * self.quant)

	def __str__(self):
		return str(self.product)

class Cart(models.Model):
	items = models.ManyToManyField(CartItem)
	val = models.FloatField(default=0.0)

	def __str__(self):
		return f'#ID {self.id}'

class Purchase(models.Model):
	delivery = models.ForeignKey(Address, on_delete = models.DO_NOTHING)
	product = models.ForeignKey(Product, on_delete = models.DO_NOTHING)
	client = models.ForeignKey(User, on_delete = models.DO_NOTHING)
	val = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
	def __str__(self):
		return f'#ID {self.id}'
