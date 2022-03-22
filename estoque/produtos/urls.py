from django.urls import path

from . import views

urlpatterns = [
    path('produtos/add', views.cadastrar, name='cadastrar'),
    path('produtos/rem', views.deletar, name='deletar'),
    path('produtos/list', views.listar, name='listar'),
    path('produtos/view', views.visualizar, name='visualizar'),
    path('produtos/update', views.atualizar, name='atualizar'),
]