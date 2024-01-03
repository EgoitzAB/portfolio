from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Secciones


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['core:home', 'core:personal']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return 1.0

    def changefreq(self, item):
        return 'yearly'

    def lastmod(self, item):
        if item == 'core:home':
            return Secciones.objects.latest('updated').updated
        elif item == 'core:personal':
            return Secciones.objects.latest('updated').updated