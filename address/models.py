from django.db import models
from authentication.models import User

class Address(models.Model):
	name = models.CharField(max_length=64)
	code = models.CharField(max_length=8)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	class Meta:
		ordering = ('name',)
	def __str__(self):
		return self.name
