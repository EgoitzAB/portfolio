from django.db import models
from django.db.models import Max
# Create your models here.
class Secciones(models.Model):
    """
    Model representing a section.

    Attributes:
        seccion (str): The name of the section.
        texto (str): The text content of the section.
        imagen (ImageField): The image associated with the section.
        created (DateTimeField): The date and time when the section was created.
        updated (DateTimeField): The date and time when the section was last updated.
    """

    seccion = models.CharField(max_length=50)
    indice = models.IntegerField(blank=True, null=True)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='secciones', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    categoria_choices = [
        ('main', 'Main'),
        ('personal', 'Personal')
    ]
    categoria = models.CharField(max_length=10, choices=categoria_choices, default='main')

    class Meta:
        ordering = ['indice']

    def save(self, *args, **kwargs):
        if self.indice is None:
            aggregate_result = Secciones.objects.aggregate(Max('indice'))
            max_indice = aggregate_result['indice__max'] if 'indice__max' in aggregate_result else 0
            self.indice = max_indice + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.seccion

class PDF(models.Model):
    file = models.FileField(upload_to='pdfs/')
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

