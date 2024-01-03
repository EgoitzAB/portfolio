from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class ContactoSitemap(Sitemap):
    priority = 0.5
    changefreq = "anually"

    def items(self):
        return ['contacto:contacto']

    def location(self, item):
        return reverse(item)