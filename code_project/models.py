from django.db import models


class Proyecto(models.Model):
    TIPO_CONTENIDO = (
        ('script', 'Script'),
        ('proyecto', 'Proyecto'),
    )

    STATUS_CHOICES = (
        ('abandonado', 'Abandonado'),
        ('finalizado', 'Finalizado'),
        ('en progreso', 'En Progreso'),
    )
    nombre = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    tipo_contenido = models.CharField(max_length=10, choices=TIPO_CONTENIDO, default='proyecto')
    url = models.URLField(max_length=200, blank=True, null=True)


class Codigo(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    pasos = models.CharField(max_length=200)
    codigo = models.TextField(blank=True, null=True)
    fotos = models.ImageField(upload_to='codigo_fotos/', blank=True, null=True)
