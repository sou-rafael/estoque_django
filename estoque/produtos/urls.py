from django.urls import path

from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('listar', views.listar, name='listar'),
    path('<int:id>', views.visualizar, name='visualizar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar'),
]