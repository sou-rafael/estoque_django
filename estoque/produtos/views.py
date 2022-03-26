from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
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

def atualizar(request):
    template_name = "produtos/atualizar.html"
    return render(request,template_name)