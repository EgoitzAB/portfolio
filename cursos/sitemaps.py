from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Curso

class CursoSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.9

    def items(self):
        return ['cursos:lista_cursos']

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        # Obtén el último curso modificado
        last_modified_course = Curso.objects.order_by('-fecha_modificado').first()
        return last_modified_course.fecha_modificado if last_modified_course else None