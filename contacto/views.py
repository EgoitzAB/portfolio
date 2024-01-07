from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm
from cookie_consent.util import get_cookie_value_from_request


class ContactoView(View):
    def get(self, request):
        form = ContactForm()
        cookies_accepted = get_cookie_value_from_request(request, "cookie-consent")
        return render(request, 'contacto/contacto.html', {'form': form, 'cookies_accepted': cookies_accepted})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Validar aceptación de cookies de reCAPTCHA
            cc = get_cookie_value_from_request(request, "cookie-consent")
            if not cc:
                messages.error(request, "Debes aceptar las cookies de AdSense")
                return redirect('contacto')
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
                    messages.error(request, "Debes pasar la prueba reCAPTCHA")
                    continue
                messages.error(request, error)

        return render(request, 'contacto/contacto.html', {'form': form})
