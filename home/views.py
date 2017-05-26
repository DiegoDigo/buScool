from django.shortcuts import render
from motorista.models import Motorista

def Home(request):
    context = {}
    return render(request, 'home.html', context)


def Pesquisa(request):
    context = {
        'motoristas': Motorista.objects.all(),
    }
    return render(request, 'pesquisa.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def detalheMotorista(request, pk):
    context = {
        'motorista': Motorista.objects.get(pk=pk)
    }
    return render(request, 'detalheMotorista.html', context)
