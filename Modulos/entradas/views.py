from django.shortcuts import render, redirect
from Modulos.inventario.models import Producto
from models import Entrada
from forms import EntradaForm
# Create your views here.


def registrar_entrada(request, **kwargs):
  if not request.user.is_anonymous():
    id = kwargs.get('pk')
    form = EntradaForm()
    if request.POST:
        form = EntradaForm(request.POST)
        if form.is_valid():
            data = form.instance.unidades
            producto = Producto.objects.get(id=id)
            producto.unidades += data
            producto.save()
            Entrada(
                producto=producto,
                unidades=int(data),
                usuario=request.user
            ).save()
            return redirect('inicio')
    context = {
        'form': form,
        'titulo' : ':: Asignar unidades ::'
    }
    return render(request, 'form.html', context)
  else:
      return redirect('entrar')


def lista_entrada (request):
    context ={
        'entrada': Entrada.objects.all()
    }
    return render(request, 'entradas.html', context)