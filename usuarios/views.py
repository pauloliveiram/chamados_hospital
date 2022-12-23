from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from .forms import CadastroUsuarioForm, AtualizarUsuarioForm, LoginUsuarioForm
from .models import Usuario

@login_required
def cadastro_usuario(request):
    if request.method == 'POST':
        cadastro_form = CadastroUsuarioForm(request.POST)
        if cadastro_form.is_valid():
            usuario = cadastro_form.create()

            if usuario.tipo_profissional == '1':
                assign_role(usuario, 'coordenador')
            if usuario.tipo_profissional == '2':
                assign_role(usuario, 'tecnico')
            if usuario.tipo_profissional == '3':
                assign_role(usuario, 'profissional')        
            
            usuario = authenticate(email = usuario.email, senha=cadastro_form.cleaned_data['senha1'])
            login(request, usuario)
            return redirect('login')

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

@csrf_protect
def login_usuario(request):

    login_usuario_form = LoginUsuarioForm()

    if request.user.is_authenticated:
        return redirect('lista_usuarios')

    else:
        if request.method == 'POST':
            login_usuario_form = LoginUsuarioForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            usuario = authenticate(request, username=username, password=password)

            if usuario is not None:
                login(request, usuario)
                return redirect('inicio_coordenador', username=username)

        else:
            login_form = LoginUsuarioForm()

    context = {
        'login_usuario_form': login_usuario_form,
    }

    return render(request, 'login_usuario.html', context) 

def logout_usuario(request):
    logout(request)
    return redirect('login_usuario')
    
def inicio_coordenador(request, username):
    context = {}
    context["data"] = Usuario.objects.get(username=username)
    return render(request, 'tela_inicial_coordenador.html', context)                              
