from django.urls import path 
from .views import cadastro_usuario, lista_usuarios, usuario_view, atualizar_usuario, remover_usuario, login_usuario, logout_usuario, inicio_coordenador

urlpatterns = [
    path('cadastro/', cadastro_usuario, name='cadastro_usuario'),
    path('login/', login_usuario, name='login_usuario'),
    path('logout/', logout_usuario, name='logout_usuario'),
    path('', lista_usuarios, name='lista_usuarios'),
    path('<id>/', usuario_view, name='usuario_view'),
    path('<id>/atualizar/', atualizar_usuario, name='atualizar_usuario'),
    path('<id>/remover/', remover_usuario, name='remover_usuario'),
    path('<username>/inicio', inicio_coordenador, name='inicio_coordenador'),
]