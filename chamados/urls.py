from django.urls import path
from .views import ChamadoCadastroView, ChamadoListView, ChamadoDetailView, ChamadoUpdateView, ChamadoDeleteView

urlpatterns = [
    path('cadastro', ChamadoCadastroView.as_view()),
    path('', ChamadoListView.as_view()),
    path('<pk>', ChamadoDetailView.as_view()),
    path('<pk>/atualizar', ChamadoUpdateView.as_view()),
    path('<pk>/apagar', ChamadoDeleteView.as_view()),
]