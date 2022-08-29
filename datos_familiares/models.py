from django.db import models

# Create your models here.

class familiares(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()
    peso_kg = models.IntegerField()
    