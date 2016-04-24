from django.shortcuts import render, redirect
from models import Producto, Categoria,  Provedor
from forms import CategoriaForm, ProvedorForm, ProdcutoForm
# Create your views here.


def inicio(request):
    if not request.user.is_anonymous():
        context = {
            'productos': Producto.objects.all()
        }
        return render(request, 'lista_productos.html', context)
    else:
        return redirect('entrar')


def lista_de_categoria(request):
    if not request.user.is_anonymous():
        context = {
            'categorias' : Categoria.objects.all()
        }
        return render(request, 'listar_categoria.html' , context)
    else:
        return redirect('entrar')


def lista_de_provedor(request):
    if not request.user.is_anonymous():
        context = {
            'provedores' : Provedor.objects.all()
        }
        return render(request, 'listar_provedor.html', context)
    else:
        return redirect('entrar')


def lista_productos_provedor(request, **kwargs):
    if not request.user.is_anonymous():
        id_provedor = kwargs.get('pk')
        context = {
            'productos': Producto.objects.filter(provedor=id_provedor)
        }
        return render(request, 'lista_productos.html', context)
    else:
        return redirect('entrar')


def lista_productos_categoria(reques, **kwargs):
    if not reques.user.is_anonymous():
        id_categoria = kwargs.get('pk')
        context={
            'productos' : Producto.objects.filter(categoria=id_categoria)
        }
        return render(reques, 'lista_productos.html', context)
    else:
        return redirect('entrar')


def crear_categoria(request):
    if not request.user.is_anonymous():
        form = CategoriaForm()
        if request.POST:
            form = CategoriaForm(request.POST)
            if form.is_valid():
             form.save()
             return redirect('categorias')
        context ={
                'form': form,
                'titulo' : ':: Crear Categoria ::'
                  }
        return render(request, 'form.html', context)
    else:
        return redirect('entrar')


def crear_provedor(request):
   if not request.user.is_anonymous():
        form = ProvedorForm()
        if request.POST:
            form = ProvedorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('proveedores')
        context ={
            'form': form,
            'titulo' : ' ::Crear Proveedor ::'
        }
        return render(request, 'form.html', context)
   else:
       return redirect('entrada')


def crear_producto(request):
    if not request.user.is_anonymous():
        form = ProdcutoForm()
        if request.POST:
            form = ProdcutoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('inicio')
        context ={
            'form': form,
            'titulo': ':: Crear Producto ::'
        }
        return render(request, 'form.html', context)
    else:
        return redirect('entrar')