from django.db import models



class Produtos(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=400)
    quantidade = models.IntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome