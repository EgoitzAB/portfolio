import re

from django import forms
from django_recaptcha.fields import ReCaptchaField
from django.core.exceptions import ValidationError

def your_phone_validator(value):
    if not re.match(r'^\+?1?\d{9,15}$', value):
        raise ValidationError('Ingrese un número de teléfono válido.')


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    apellidos = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    telefono = forms.CharField(max_length=20, required=False, validators=[your_phone_validator], widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje'}))
    captcha = ReCaptchaField()