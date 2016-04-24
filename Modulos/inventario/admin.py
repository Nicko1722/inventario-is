from django.contrib import admin
from .models import Producto, Provedor, Categoria
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['id', 'nombre']


@admin.register(Provedor)
class ProvedorAdmin(admin.ModelAdmin):

    list_display = ['id', 'nombre']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):

    list_display = ['id', 'nombre', 'categoria',
                    'provedor', 'unidades']

