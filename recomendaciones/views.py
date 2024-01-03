from django.views import View
from .models import Recomendacion
from django.shortcuts import render


class RecomendacionesView(View):
    def get(self, request):
        recomendaciones = Recomendacion.objects.all()
        return render(request, 'recomendaciones/recomendaciones.html', {'recomendaciones': recomendaciones})

