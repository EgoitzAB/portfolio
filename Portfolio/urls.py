from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from code_project.sitemaps import ProyectoSitemap
from core.sitemaps import StaticViewSitemap as Core_app
from cursos.sitemaps import CursoSitemap
from recomendaciones.sitemaps import RecomendadosSitemap
from contacto.sitemaps import ContactoSitemap

sitemaps = {
    'proyectos': ProyectoSitemap,
    'core': Core_app,
    'cursos': CursoSitemap,
    'recomendados': RecomendadosSitemap,
    'contacto': ContactoSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('cursos/', include("cursos.urls")),
    path('proyectos-código/', include("code_project.urls")),
    path('contacto/', include("contacto.urls")),
    path('recomendados/', include("recomendaciones.urls")),
    path('cookies/', include('cookie_consent.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
