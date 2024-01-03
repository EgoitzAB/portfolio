from django.urls import path
from .views import RecomendacionesView

app_name = 'recomendaciones'

urlpatterns = [
    path('', RecomendacionesView.as_view(), name='recomendados'),
]