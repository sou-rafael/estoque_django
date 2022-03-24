from django.urls import path

from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path('add', views.cadastrar, name='cadastrar'),
    path('rem', views.deletar, name='deletar'),
    path('list', views.listar, name='listar'),
    path('view', views.visualizar, name='visualizar'),
    path('update', views.atualizar, name='atualizar'),
]