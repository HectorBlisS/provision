from django.db import models
from django.utils import timezone
from provision import settings


class NuevaPregunta(models.Model):

	nombre=models.CharField(max_length=50)
	tel=models.CharField(max_length=15)
	mail=models.EmailField(max_length=254)
	size=models.CharField(max_length=25,blank=True,null=True)
	plazo=models.CharField(max_length=25,blank=True,null=True)
	date=models.DateField(default=timezone.now)
	comentario=models.TextField(blank=True,null=True)
	cerrado=models.BooleanField(default=False)
	contacto=models.DateField(default=None,blank=True,null=True)

	def __str__(self):
		return self.nombre

class Size(models.Model):
	nombre=models.CharField(max_length=50)
	size=models.IntegerField()

	def __str__(self):
		return self.nombre

class Plazo(models.Model):
	nombre=models.CharField(max_length=50)
	plazo=models.IntegerField()

	def __str__(self):
		return self.nombre
