from django.db import models

# Create your models here.
class Codigo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    field1 = models.CharField(max_length=50)
    field2 = models.IntegerField()
    field3 = models.BooleanField(default=False)
    # Agrega más campos aquí

    # Campos descriptivos
    client = models.CharField(max_length=100)  # Cliente del proyecto
    status = models.CharField(max_length=50)  # Estado del proyecto (en progreso, completado, etc.)
    budget = models.DecimalField(max_digits=8, decimal_places=2)  # Presupuesto del proyecto
    deadline = models.DateField()  # Fecha límite del proyecto
    # Agrega más campos descriptivos según tus necesidades
