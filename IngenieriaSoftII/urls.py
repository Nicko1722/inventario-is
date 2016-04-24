"""IngenieriaSoftII URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Modulos.inventario.views.inicio', name='inicio'),
    url(r'^categoria', 'Modulos.inventario.views.lista_de_categoria', name='categorias'),
     url(r'^proveedores', 'Modulos.inventario.views.lista_de_provedor', name='proveedores'),
    url(r'^productos-provedor/(?P<pk>\d+)/', 'Modulos.inventario.views.lista_productos_provedor', name='productos_provedor'),
    url(r'^productos-categoria/(?P<pk>\d+)/', 'Modulos.inventario.views.lista_productos_categoria', name='productos_categoria'),
    url(r'^crear_categoria', 'Modulos.inventario.views.crear_categoria', name='crear_categoria'),
    url(r'^crear_proveedor', 'Modulos.inventario.views.crear_provedor', name='crear_proveedor'),
    url(r'^crear_producto', 'Modulos.inventario.views.crear_producto', name='crear_producto'),

    url(r'^nueva-entrada/(?P<pk>\d+)/', 'Modulos.entradas.views.registrar_entrada', name='nueva_entrada'),
    url(r'^nueva-salida/(?P<pk>\d+)/', 'Modulos.salidas.views.registrar_salida', name='nueva_salida'),
     url(r'^entrada', 'Modulos.entradas.views.lista_entrada', name='entrada'),
     url(r'^salida', 'Modulos.salidas.views.lista_salida', name='salida'),

    url(r'^login/', 'Modulos.usuarios.views.log_in', name='entrar'),
    url(r'^logout/', 'Modulos.usuarios.views.salir', name='salir'),

]
