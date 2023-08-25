from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')


def cadastro(request):
    return render(request,'cadastro/cadastro_filmes.html')

def lista(request):
    return render(request,'lista/lista_filmes.html')
    