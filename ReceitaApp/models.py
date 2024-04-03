from django.db import models

# Create your models here.
class Categoria(models.Model):
    Nome = models.CharField(max_length=30)
        

class Receita(models.Model):
    opcao=[
      ("Fácil", "Fácil"),
      ("Moderado", "Moderado"),
      ("Dificil", "Dificil"),
   ]
       
    Nome = models.CharField(max_length=50)
    Ingredientes = models.TextField(max_length=2000)
    Modo_de_Preparo = models.TextField(max_length=8000)
    Grau_de_Dificuldade = models.CharField(max_length=10, blank=True, null=True, choices=opcao)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
