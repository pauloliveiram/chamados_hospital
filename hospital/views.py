from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .models import Equipamento, Setor
from .forms import EquipamentoForm, SetorForm

def create_equipamento_view(request):

    context = {}

    equipamentoForm = EquipamentoForm(request.POST or None)
    if equipamentoForm.is_valid():
        equipamentoForm.save()

    context['form'] = equipamentoForm
    return render(request, "create_equipamento.html", context)

def list_equipamentos(request):

    context = {}

    context["dataset"] = Equipamento.objects.all()
    return render(request, 'list_equipamentos.html', context)
    
def equipamento_view(request, id):
    context = {}

    context["data"] = Equipamento.objects.get(numero_serie=id)
    return render(request, "detail_equipamento.html", context)     

def update_equipamento(request, id):
    context = {}

    obj = get_object_or_404(Equipamento, numero_serie = id)       

    form = EquipamentoForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/equipamentos/"+id)

    context["form"] = form
    return render(request, 'update_equipamento.html', context)

def delete_equipamento(request, id):
    context = {}

    obj = get_object_or_404(Equipamento, numero_serie = id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('/')

    return render(request, 'delete_equipamento.html', context)        


class SetorCadastroView(CreateView):
    model = Setor
    fields = ['nome', 'quantidade_leitos']
    success_url = '/setores'

class SetorListView(ListView):
    model = Setor

class SetorDetailView(DetailView):
    model = Setor

class SetorUpdateView(UpdateView):
    model = Setor
    fields = ['nome', 'quantidade_leitos']
    success_url = '/setores'

class SetorDeleteView(DeleteView):
    model = Setor
    success_url = '/setores'    