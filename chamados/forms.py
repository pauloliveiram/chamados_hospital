from django import forms
from .models import Chamado
from usuarios.models import Usuario

class ChamadoForm(forms.ModelForm):
     class Meta:
        model = Chamado
        fields = ['problema', 'descricao']
 
class ChamadoUpdateForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['problema', 'descricao', 'data_fechamento', 'custo_manutencao', 'tecnico']