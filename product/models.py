from django.db import models
from authentication.models import User

class Category(models.Model):
	name = models.CharField(max_length=48)
	slug = models.SlugField()

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	name = models.CharField(max_length=48)
	slug = models.SlugField()
	desc = models.TextField(blank=True, null=True)
	price = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ("-created_at",)

	def __str__(self):
		return self.name

class Address(models.Model):
	name = models.CharField(max_length=64)
	code = models.CharField(max_length=8)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name


