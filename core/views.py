from django.shortcuts import render


def index(request):
    context = {
        'curso': 'programção web',
        'outro': 'Django e Massa'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')