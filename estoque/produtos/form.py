from django.forms import ModelForm
from .models import Produtos

class ProdForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'descricao', 'quantidade']