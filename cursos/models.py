from django.db import models
from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100, blank=True)
    identificador = models.CharField(max_length=50, blank=True)
    url = models.URLField(blank=True)
    archivo = models.ImageField(upload_to='archivos/', blank=True)
    descripcion = models.TextField()
    horas = models.PositiveIntegerField()
    habilidades = models.ManyToManyField('Habilidad')
    tags = TaggableManager()
    fecha_modificado = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('cursos:lista_cursos')


class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

