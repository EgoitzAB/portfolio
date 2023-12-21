from django.contrib import admin
from .models import Codigo, Proyecto

class CodigoInline(admin.TabularInline):
    model = Codigo

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'status', 'tipo_contenido')
    inlines = [CodigoInline]

@admin.register(Codigo)
class CodigoAdmin(admin.ModelAdmin):
    pass
