from django.db import models
from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    identificador = models.CharField(max_length=50, blank=True)
    url = models.URLField(blank=True)
    archivo = models.FileField(upload_to='archivos/', blank=True)
    descripcion = models.TextField()
    horas = models.PositiveIntegerField()
    habilidades = models.ManyToManyField('Habilidad')

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)

