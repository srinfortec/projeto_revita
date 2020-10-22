from django.shortcuts import render, redirect
from . forms import FormClientes
from . models import Clientes

# Create your views here.

def home(request):
    return render(request, 'cliente/home.html')


def cadastro(request):
    if request.method == 'POST':
        cliente = Clientes()

        cliente.nome_completo = request.POST.get("nome_completo")
        cliente.data_nascimento = request.POST.get("data_nascimento")
        cliente.endereco= request.POST.get("endereco")
        cliente.whatsapp = request.POST.get("whatsapp")
        cliente.email = request.POST.get("email")
        cliente.problema = request.POST.get("problema")
        cliente.dia_semana   = request.POST.get("dia_semana")
        cliente.horario = request.POST.get("horario")

        cliente.save()
        return redirect("home")
    return render(request,"cliente/cadastro.html")


def listar(request):
    clientes = Clientes.objects.all()

    return render(request, 'cliente/lista_clientes.html', {
        'clientes': clientes
    })