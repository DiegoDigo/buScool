from django.shortcuts import render


def Home(request):
    return render(request, 'home.html', {})


def Pesquisa(request):
    pesquisa = "Luiza Salete Junca de Almeida"
    return render(request, 'pesquisa.html', {'pesquisado': pesquisa})
