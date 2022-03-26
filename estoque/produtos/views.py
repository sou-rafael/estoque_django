from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Produtos

def index(request):
    template_name = "produtos/base.html"
    return render(request,template_name)

def cadastrar(request):
    template_name = "produtos/cadastrar.html"
    return render(request,template_name)

def deletar(request):
    template_name = "produtos/deletar.html"
    return render(request,template_name)

def listar(request):
    template_name = "produtos/listar.html"
    return render(request,template_name)

# Criando a funcao visualizar
def visualizar(request):
    template_name = "produtos/visualizar.html"
    produtos = Produtos.objects.all()
    return render(request,template_name, {'produtos': produtos})

def atualizar(request):
    template_name = "produtos/atualizar.html"
    return render(request,template_name)