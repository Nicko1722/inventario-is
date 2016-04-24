from django.contrib import admin
from .models import Entrada
# Register your models here.
@admin.register(Entrada)
class EntradaAdmin (admin.ModelAdmin):

    list_display = [ 'usuario', 'producto', 'fecha', 'unidades' ]