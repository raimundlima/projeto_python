from django.shortcuts import render
from .models import Filme

# Create your views here.

def home(request):
    return render(request,'home.html')


def cadastro(request):
    return render(request,'cadastro/cadastro_filmes.html')


def lista_filmes(request):
    filmes = []
    if request.method =='GET':
        filmes = Filme.objects.all()
    return render(request,'lista\lista_filmes.html',{'filmes':filmes})






    
    #exibir todos os filmes já cadastrados em uma nova pagina

    