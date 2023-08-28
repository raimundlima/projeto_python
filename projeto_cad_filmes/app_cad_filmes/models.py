from django.db import models

# Create your models here.
from django.db import models

class Filme(models.Model):
    id_filme = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    genero = models.CharField(max_length=50)
    ano_lancamento = models.IntegerField()
    Sinopse = models.TextField(max_length=250)
    capa = models.CharField(max_length=250)

   
