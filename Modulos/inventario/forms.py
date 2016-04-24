__author__ = 'Nicolas'
from django import forms
from models import Categoria
from models import Provedor, Producto


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nombre',]


class ProvedorForm(forms.ModelForm):

    class Meta:
        model = Provedor
        fields = ['nombre',]

class ProdcutoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre','categoria', 'provedor', 'unidades']

