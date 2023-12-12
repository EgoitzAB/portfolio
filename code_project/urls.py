from django.urls import path
from . import views

urlpatterns = [
    path('código/<int:pk>/', views.CodeDetailView.as_view(), name='code_detail'),
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('proyectos/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
]

