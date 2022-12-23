from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .forms import ChamadoUpdateForm, ChamadoForm
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator, has_permission_decorator

from .models import Chamado
from usuarios.models import Usuario


#class ChamadoCadastroView(CreateView):
 #   model = Chamado
  #  fields = ['problema', 'descricao', 'pessoa_solicitante']
   # #assign_role(Usuario, 'coordenador')
    #success_url = '/chamados/cadastro'

@login_required
@has_role_decorator(['coordenador', 'profissional'])
def cadastro_chamado(request):
    if request.method == 'POST':
        chamadoForm = ChamadoForm(request.POST or None)
        if chamadoForm.is_valid():
            chamadoForm.save()
            return redirect('')

    else:
        chamadoForm = ChamadoForm()

    context = {'chamadoForm':chamadoForm}

    return render(request, 'chamados/chamado_form.html', context)    

#@has_role_decorator(['coordenador'])
def list_chamados(request):

    context = {}

    context["dataset"] = Chamado.objects.all()
    return render(request, 'chamados/chamado_list.html', context)

@has_role_decorator(['coordenador'])    
def chamado_view(request, id):
    context = {}

    context["data"] = Chamado.objects.get(numero_serie=id)
    return render(request, "chamados/chamado_detail.html", context)     

@has_role_decorator(['coordenador'])
def update_chamado(request, id):
    context = {}

    obj = get_object_or_404(Chamado, id = id)       

    chamadoUpdateForm = ChamadoUpdateForm(request.POST or None, instance = obj)

    if chamadoUpdateForm.is_valid():
        chamadoUpdateForm.save()
        return HttpResponseRedirect("/chamados/"+id)

    context["chamadoUpdateForm"] = chamadoUpdateForm
    return render(request, 'chamados/update_chamado.html', context)

@has_role_decorator(['coordenador'])
def delete_chamado(request, id):
    context = {}

    obj = get_object_or_404(Chamado, numero_serie = id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('/')

    return render(request, 'chamados/chamado_confirm_delete.html', context)