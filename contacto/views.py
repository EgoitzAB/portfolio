from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm


class ContactoView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contacto/contacto.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            email = EmailMessage(
                'Nuevo mensaje de contacto',
                'De: {0} {1}\nEmail: {2}\n\n{3}'.format(
                    form.cleaned_data.get('nombre'),
                    form.cleaned_data.get('apellidos'),
                    form.cleaned_data.get('email'),
                    form.cleaned_data.get('mensaje'),
                ),
                to=['meimportaunamierda@protonmail.com']
            )
            email.send()
            return redirect('contacto:exito')
        else:
            for error in form.errors.values():
                messages.error(request, error)

        return render(request, 'contacto/contacto.html', {'form': form})

class ExitoView(View):
    def get(self, request):
        return render(request, 'contacto/exito.html')