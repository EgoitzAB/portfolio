from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm


def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = EmailMessage(
                'Nuevo mensaje de contacto',
                'De: {0} {1}\nEmail: {2}\nTeléfono: {3}\n\n{4}'.format(
                    form.cleaned_data.get('nombre'),
                    form.cleaned_data.get('apellidos'),
                    form.cleaned_data.get('email'),
                    form.cleaned_data.get('telefono'),
                    form.cleaned_data.get('mensaje'),
                ),
                to=['meimportaunamierda@protonmail.com']
            )
            email.send()
            return redirect('contacto')
        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                messages.error(request, error)
    else:
        form = ContactForm()

    return render(request, 'contacto/contacto.html', {'form': form})