from django.db import models

class Recomendacion(models.Model):
    categoria_choices = [
        ('libro', 'Libro'),
        ('servicio', 'Servicio'),
        ('widget', 'Widget'),
    ]
    categoria = models.CharField(max_length=255, choices=categoria_choices, default='libro')
    titulo = models.CharField(max_length=255)
    paginas = models.IntegerField(blank=True, null=True)
    autor = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)
    foto = models.ImageField(upload_to='recomendaciones/', blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    caracteristicas = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo