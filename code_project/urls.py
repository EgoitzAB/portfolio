from django.urls import path
from . import views

app_name = 'code_project'

urlpatterns = [
    path('<int:proyecto_id>/', views.ProyectoDetailView.as_view(), name='proyecto_detail'),
    path('', views.ProjectListView.as_view(), name='lista_proyectos'),
]

