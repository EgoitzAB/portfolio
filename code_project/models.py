from django.db import models
from django.db.models import Max


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
    indice = models.IntegerField(blank=True, null=True)  # Permitir que el índice sea nulo o en blanco
    pasos = models.CharField(max_length=200)
    codigo = models.TextField(blank=True, null=True)
    fotos = models.ImageField(upload_to='codigo_fotos/', blank=True, null=True)

    class Meta:
        ordering = ['indice']

    def save(self, *args, **kwargs):
        # Si el índice no se ha establecido manualmente
        if self.indice is None:
            # Calcular el próximo índice basándose en el número actual de registros Codigo
            aggregate_result = Codigo.objects.filter(proyecto=self.proyecto).aggregate(Max('indice'))
            max_indice = aggregate_result['indice'] if 'indice' in aggregate_result else 0
            self.indice = max_indice + 1
        super().save(*args, **kwargs)  # Llamar al método save original