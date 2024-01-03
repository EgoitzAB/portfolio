from django.contrib.sitemaps import Sitemap
from .models import Proyecto

class ProyectoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Proyecto.objects.all()

    def lastmod(self, obj):
        return obj.fecha_modificado