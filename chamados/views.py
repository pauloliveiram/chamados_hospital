from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .models import Chamado

class ChamadoCadastroView(CreateView):
    model = Chamado
    fields = ['problema', 'descricao', 'pessoa_solicitante']
    success_url = '/chamados/cadastro'

class ChamadoListView(ListView):    
    model = Chamado

class ChamadoDetailView(DetailView):
    model = Chamado

class ChamadoUpdateView(UpdateView):
    model = Chamado
    fields = ['status', 'data_abertura', 'data_fechamento', 'custo_manutencao']
    success_url = '/chamados'

class ChamadoDeleteView(DeleteView):
    model = Chamado
    success_url = '/chamados'            