from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Secciones

# Create your views here.
class HomeView(TemplateView):
    """
    A view that renders the home page.

    Attributes:
        model (Model): The model associated with the view.
        template_name (str): The name of the template to be rendered.

    Methods:
        get_context_data(**kwargs): Retrieves the context data for the view.

    """

    model = Secciones
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        """
        Retrieves the context data for the view.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The context data for the view.

        """
        context = super().get_context_data(**kwargs)
        context['secciones'] = Secciones.objects.all()
        return context
