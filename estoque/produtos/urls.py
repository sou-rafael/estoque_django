from django.urls import path

from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('deletar', views.deletar, name='deletar'),
    path('listar', views.listar, name='listar'),
    path('visualizar', views.visualizar, name='visualizar'),
    path('atualizar', views.atualizar, name='atualizar'),
]