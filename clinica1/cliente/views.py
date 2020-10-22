from django.shortcuts import render, redirect
from . forms import FormClientes
from . models import Clientes

# Create your views here.

def home(request):
    return render(request, 'cliente/home.html')


def cadastro(request):
    return render(request, 'cliente/cadastro.html')

def cadastrar(request):
    form = FormClientes(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'cliente/cadastrar.html',{'form': form})


def listar(request):
    clientes = Clientes.objects.all()

    return render(request, 'cliente/lista_clientes.html', {
        'clientes': clientes
    })