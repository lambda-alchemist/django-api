from django.db import models
from authentication.models import User

class Address(models.Model):
	name = models.CharField(max_length=64)
	code = models.CharField(max_length=8)
	class Meta:
		ordering = ('name',)
	def __str__(self):
		return self.name
