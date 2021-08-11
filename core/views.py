from django.shortcuts import render
from .models import Produto


def index(request):
    print(dir(request))
    print(request)
    produtos = Produto.objects.all()
    context = {
        'curso': 'programação web',
        'outro': 'Django e Massa',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)