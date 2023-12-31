from django.views.generic import ListView
from .models import Curso

class CursosListView(ListView):
    """
    View that displays a list of Curso objects.

    Attributes:
        model (Model): The model class to use for retrieving Curso objects.
        template_name (str): The name of the template to use for rendering the view.
        context_object_name (str): The name of the variable to use for the list of Curso objects in the template context.
        paginate_by (int): The number of Curso objects to display per page.

    Methods:
        get_queryset(): Returns the queryset of Curso objects to be displayed.
    """
    model = Curso
    template_name = 'cursos/lista_cursos.html'
    context_object_name = 'cursos'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        """
        Retrieves the context data for the view.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The context data for the view.

        """
        context = super().get_context_data(**kwargs)
        context['tags'] = self.get_tags()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_slug = self.kwargs.get('tag_slug', None)
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)
        return queryset

    def get_tags(self):
        return Curso.objects.values_list('tags__name', flat=True).distinct()


class CursoTagListView(ListView):
    model = Curso
    template_name = 'cursos/lista_cursos.html'
    context_object_name = 'cursos'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)
        return queryset
