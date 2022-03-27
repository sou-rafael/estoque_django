from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .form import ProdForm
from .models import Produtos

def index(request):
    template_name = "produtos/base.html"
    return render(request,template_name)

def listar(request):
    produtos = Produtos.objects.all().order_by('-data_cadastro')
    return render(request,"produtos/listar.html", {'produtos': produtos})

def visualizar(request, id):
    produto = get_object_or_404(Produtos, pk=id)
    return render(request,"produtos/visualizar.html", {'produto': produto})

def cadastrar(request):
    if request.method == 'POST':
        form = ProdForm(request.POST)
        if form.is_valid():
            produto = form.save()
            return redirect('/')
    else:
        form = ProdForm()
    return render(request, "produtos/cadastrar.html", {'form': form} )

#############################
def atualizar(request, id):
    novo = get_object_or_404(Produtos, pk=id)
    form = ProdForm(instance=novo)

    if(request.method == 'POST'):
        form = ProdForm(request.POST, instance = novo)
        if(form.is_valid()):
            novo.save()
            return redirect('/')
        else:
            return render(request, "produtos/atualizar.html", {'form':form, 'novo': novo})
    else:
        return render(request, "produtos/atualizar.html", {'form':form, 'novo': novo})
#########################
def deletar(request):
    template_name = "produtos/deletar.html"
    return render(request,template_name)