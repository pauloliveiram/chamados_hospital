"""chamado_hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from hospital.views import create_equipamento_view, list_equipamentos, equipamento_view, update_equipamento, delete_equipamento, SetorCadastroView, SetorListView, SetorDetailView, SetorUpdateView, SetorDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamentos/cadastro', create_equipamento_view),
    path('equipamentos', list_equipamentos),
    path('equipamentos/<id>', equipamento_view),
    path('equipamentos/<id>/atualizar', update_equipamento),
    path('equipamentos/<id>/apagar', delete_equipamento),
    path('setores/cadastro', SetorCadastroView.as_view()),
    path('setores', SetorListView.as_view()),
    path('setores/<pk>', SetorDetailView.as_view()),
    path('setores/<pk>/atualizar', SetorUpdateView.as_view()),
    path('setores/<pk>/apagar', SetorDeleteView.as_view()),
    path('chamados/', include('chamados.urls')),
    path('usuarios/',include('usuarios.urls'))
]
