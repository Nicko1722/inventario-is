__author__ = 'Nicolas'
from django import forms
from models import Entrada

class EntradaForm(forms.ModelForm):

    class Meta:
        model = Entrada
        fields = (
            'unidades',
        )
