from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.

def log_in(request):
    titulo = 'Cuke! - Todo List'
    context = {'titulo' : titulo , 'panel':False}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('inicio')
            else:
                context = {'titulo' : titulo , 'msj':'El usuario ha sido desactivado :(','panel':True}
        else:
            context = {'titulo' : titulo ,'msj':'Usuario o Password incorrecta','panel':True}
    return render(request,'login.html', context)


def salir(request):
    logout(request)
    return redirect('entrar')