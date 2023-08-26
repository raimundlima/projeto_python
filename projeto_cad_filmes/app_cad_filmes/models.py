from django.db import models

# Create your models here.
from django.db import models

class Filme(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano_lancamento = models.IntegerField()
    Sinopse = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
