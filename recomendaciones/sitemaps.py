from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Recomendacion

class RecomendadosSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return ['recomendaciones:recomendados']

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        # Obtén el último objeto Recomendado modificado
        last_modified_recomendado = Recomendacion.objects.order_by('-fecha_modificado').first()
        return last_modified_recomendado.fecha_modificado if last_modified_recomendado else None