from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Secciones
from cookie_consent.util import get_cookie_value_from_request
import uuid


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

    def get(self, request, *args, **kwargs):
        cc = get_cookie_value_from_request(request, "mycookies")
        if not cc:
            response = super().get(request, *args, **kwargs)
            value = str(uuid.uuid4())  # Generate a UUID4 value
            response.set_cookie("mycookies", value)
            return response
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Retrieves the context data for the view.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The context data for the view.

        """
        context = super().get_context_data(**kwargs)
        context['secciones'] = Secciones.objects.filter(categoria='main')
        context['presentacion'] = Secciones.objects.get(seccion='presentacion')
        return context

class PersonalView(TemplateView):
    """
    A view that renders the personal page.

    Attributes:
        model (Model): The model associated with the view.
        template_name (str): The name of the template to be rendered.

    Methods:
        get_context_data(**kwargs): Retrieves the context data for the view.

    """

    model = Secciones
    template_name = "core/personal.html"

    def get_context_data(self, **kwargs):
        """
        Retrieves the context data for the view.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The context data for the view.

        """
        context = super().get_context_data(**kwargs)
        context['secciones'] = Secciones.objects.filter(categoria='personal')
        return context
