from django.contrib import admin
from .models import Curso, Habilidad

class CursoAdmin(admin.ModelAdmin):
    """
    Admin class for managing Curso model. Added habilities to Curso models.

    Attributes:
        filter_horizontal (tuple): A tuple of fields to be displayed as horizontal filter.

    """
    filter_horizontal = ('habilidades',)

admin.site.register(Curso, CursoAdmin)
admin.site.register(Habilidad)



