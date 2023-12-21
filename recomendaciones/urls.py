from django.urls import path
from .views import RecomendacionesView

urlpatterns = [
    path('', RecomendacionesView.as_view(), name='recomendados'),
]