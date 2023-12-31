from .forms import ContactForm

def add_form_to_context(request):
    return {'form': ContactForm()}
