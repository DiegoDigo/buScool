from django.shortcuts import render


def Home(request):
    context = {}
    return render(request, 'home.html', context)


def Pesquisa(request):
    context = {
        'pesquisa': "Luiza Salete Junca de Almeida",
        'vagas': 10
    }
    return render(request, 'pesquisa.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)