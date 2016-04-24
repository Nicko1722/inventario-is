from django.shortcuts import render, redirect
from Modulos.inventario.models import Producto
from models import Salida
from form import SalidaForm
# Create your views here.


def registrar_salida(request, **kwargs):

    if not request.user.is_anonymous():
        error = False
        unidades = None
        id = kwargs.get('pk')
        form = SalidaForm()
        data = None
        if request.POST:
            form = SalidaForm(request.POST)
            if form.is_valid():
                data = form.instance.unidades
                producto = Producto.objects.get(id=id)
                if producto.unidades - data >= 0:
                    producto.unidades -= data
                    producto.save()
                    Salida(
                        producto=producto,
                        unidades=int(data),
                        usuario=request.user,
                        conceptos=form.instance.conceptos
                    ).save()
                    return redirect('inicio')
                else:
                     error = True
                     unidades = producto.unidades
        context = {
            'form': form,
            'error': error,
            'unidades': unidades,
            'titulo': ':: Asignar unidades ::',
            'data': data
        }
        return render(request, 'form.html', context)
    else:
        return redirect('entrar')


def lista_salida (request):
    if not request.user.is_anonymous():
        context = {
            'salida': Salida.objects.all()
        }
        return render(request, 'salidas.html', context)
    else:
        return redirect('entrar')