from django.urls import path
from .views import cadastro_chamado, list_chamados, update_chamado, delete_chamado, chamado_view

urlpatterns = [
    path('cadastro', cadastro_chamado, name='cadastro_chamado'),
    path('', list_chamados, name='list_chamados'),
    path('<pk>', chamado_view, name='chamado_view'),
    path('<id>/atualizar', update_chamado, name='update_chamado'),
    path('<pk>/apagar', delete_chamado, name='delete_chamado'),
]