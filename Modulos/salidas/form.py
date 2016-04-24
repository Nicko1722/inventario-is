__author__ = 'Nicolas'
from django import forms
from models import Salida


class SalidaForm(forms.ModelForm):

    class Meta:
        model = Salida
        fields = (
            'unidades', 'conceptos',
        )