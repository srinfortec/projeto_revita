from django.shortcuts import render, redirect # Redirecionar pagina
from . models import Clientes # importar models de cliente
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'cliente/home.html')  # retorna para endereço home page


def cadastro(request):       # função
    if request.method == 'POST':
        cliente = Clientes()

        cliente.nome_completo = request.POST.get("nome_completo")       #postar informação no banco
        cliente.data_nascimento = request.POST.get("data_nascimento")
        cliente.endereco= request.POST.get("endereco")
        cliente.whatsapp = request.POST.get("whatsapp")
        cliente.email = request.POST.get("email")
        cliente.problema = request.POST.get("problema")
        cliente.dia_semana   = request.POST.get("dia_semana")
        cliente.horario = request.POST.get("horario")

        cliente.save()
        messages.success(request, "Consulta marcada com sucesso!")
        return redirect("home")
    return render(request,"cliente/cadastro.html")


def listar(request):
    clientes = Clientes.objects.all()

    return render(request, 'cliente/lista_clientes.html', {
        'clientes': clientes
    })