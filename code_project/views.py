from django.shortcuts import render, get_object_or_404
from .models import Codigo, Proyecto
from django.views.generic import ListView, DetailView


class ProjectListView(ListView):
    model = Proyecto
    template_name = 'code_project/proyecto_list.html'
    context_object_name = 'proyectos'
    paginate_by = 8


class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'code_project/proyecto_detalle.html'
    context_object_name = 'code'
    pk_url_kwarg = 'proyecto_id'

