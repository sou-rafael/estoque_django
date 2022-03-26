from http.client import HTTPResponse
<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
=======
from django.shortcuts import render, get_object_or_404
>>>>>>> 83d3f3e3a79d518410ffffc19255757e48c8e4ed
from .models import Produtos

def index(request):
    template_name = "produtos/base.html"
    return render(request,template_name)

def listar(request):
    produtos = Produtos.objects.all()
    return render(request,"produtos/listar.html", {'produtos': produtos})

def visualizar(request):
    produto = get_object_or_404(Produtos, pk=id)
    return render(request,"produtos/visualizar.html", {'produto': produto})

def cadastrar(request):
    template_name = "produtos/cadastrar.html"
    return render(request,template_name)

def deletar(request):
    template_name = "produtos/deletar.html"
    return render(request,template_name)

<<<<<<< HEAD
def listar(request):
    template_name = "produtos/listar.html"
    return render(request,template_name)

# Criando a funcao visualizar
def visualizar(request):
    template_name = "produtos/visualizar.html"
    produtos = Produtos.objects.all()
    return render(request,template_name, {'produtos': produtos})

=======
>>>>>>> 83d3f3e3a79d518410ffffc19255757e48c8e4ed
def atualizar(request):
    template_name = "produtos/atualizar.html"
    return render(request,template_name)