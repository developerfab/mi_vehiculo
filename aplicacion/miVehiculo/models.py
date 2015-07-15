from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
	"""
	Es la extension del usuario por defecto de django. Almacena los valores extra de tipo de licencia, documento, propietario 
	"""
	tipo_licencia = models.CharField(max_length=2)
	propietario = models.BooleanField(default=False)
	documento = models.IntegerField()
	fecha_licencia = models.DateField()
	

class Vehiculo(models.Model):
	"""
	Es el vehiculo relacionado a un usuario especifico
	"""
	propietario = models.ForeignKey(Usuario)
	tipo = models.CharField(max_length=60)
	placa = models.CharField(max_length=6)
	marca = models.CharField(max_length=50, default="")

class Impuesto(models.Model):
	"""
	es la lista de impuestos 
	"""
	impuesto = models.CharField(max_length=50)

class FechaImpuesto(models.Model):
	"""
	es la fecha de pago de un impuesto relacionada con un vehiculo
	"""
	vehiculo = models.ForeignKey(Vehiculo)
	impuesto = models.ForeignKey(Impuesto)
	fecha = models.DateField()


