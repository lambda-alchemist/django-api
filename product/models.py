from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=48)
	slug = models.SlugField()

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name
