from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .forms import CadastroUsuarioForm, AtualizarUsuarioForm
from .models import Usuario

def cadastro_usuario(request):
    if request.method == 'POST':
        cadastro_form = CadastroUsuarioForm(request.POST)
        if cadastro_form.is_valid():
            usuario = cadastro_form.create()
            usuario = authenticate(email = usuario.email, senha=cadastro_form.cleaned_data['senha1'])
            login(request, usuario)
            return redirect('')

    else:
        cadastro_form = CadastroUsuarioForm()

    context = {'cadastro_form':cadastro_form}

    return render(request, 'cadastro_usuario.html', context)

def lista_usuarios(request):
    context = {}

    context["dataset"] = Usuario.objects.all()
    return render(request, 'lista_usuarios.html', context)

def usuario_view(request, id):
    context = {}
    context["data"] = Usuario.objects.get(id=id)
    return render(request, 'usuario_view.html', context)

def atualizar_usuario(request, id):
    context = {}

    usuario = get_object_or_404(Usuario, id=id)
    form = AtualizarUsuarioForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/usuarios")

    context["form"] = form
    return render(request, 'atualizar_usuario.html', context)
    
def remover_usuario(request, id):
    context = {}
    usuario = get_object_or_404(Usuario, id=id)
    context["data"] = get_object_or_404(Usuario, id=id)

    if request.method == "POST":
        usuario.delete()
        return HttpResponseRedirect("/usuarios")

    return render(request, 'remover_usuario.html', context)                                    