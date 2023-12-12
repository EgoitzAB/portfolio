from django.shortcuts import render, get_object_or_404
from .models import Codigo
from django.views.generic import ListView, DetailView


class ProjectListView(ListView):
    model = Codigo
    template_name = 'project_list.html'
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Codigo
    template_name = 'project_detail.html'
    context_object_name = 'project'
    pk_url_kwarg = 'project_id'


class CodeDetailView(DetailView):
    model = Codigo
    template_name = 'code_detail.html'
    context_object_name = 'code'
    pk_url_kwarg = 'code_id'

