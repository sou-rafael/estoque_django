from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def cadastrar(request):
    return HTTPResponse('Cadastrar')

def deletar(request):
    return HTTPResponse('Deletar')

def listar(request):
    return HTTPResponse('Listar')

def visualizar(request):
    return HTTPResponse('Visualizar')

def atualizar(request):
    return HTTPResponse('Atualizar')