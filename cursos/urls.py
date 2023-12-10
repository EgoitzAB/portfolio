from django.urls import path
from .views import CursosListView

"""
List of URL patterns for the cursos app.

This module defines the URL patterns for the cursos app. It includes the following patterns:

- `/cursos/`: This pattern maps to the `CursosListView` view and is named `lista_cursos`.

"""
aap_name = 'cursos'

urlpatterns = [
    path('', CursosListView.as_view(), name='lista_cursos'),
]



