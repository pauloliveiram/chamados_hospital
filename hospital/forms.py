from django import forms
from .models import Equipamento, Setor

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'numero_serie']

class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ['nome', 'quantidade_leitos']        