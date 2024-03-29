from django.db import models
from usuarios.models import Usuario

class Chamado(models.Model):
    STATUS_CHOICES = (
        ('S', 'Solicitado'),
        ('A', 'Atendido'),
        ('F', 'Fechado')
        )

    problema = models.CharField("Problema", max_length=255, blank=False)
    descricao = models.TextField("Descrição do problema")
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(null=True)
    tempo_manutencao = models.DateTimeField(null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='S', blank=False, null=False)
    pessoa_solicitante = models.CharField(max_length=255, blank=False)
    custo_manutencao = models.DecimalField(max_digits=25, decimal_places=2, default=0, null=True)
    tecnico = models.ForeignKey(Usuario, limit_choices_to={'tipo_profissional': '2'}, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Chamado'
        verbose_name = 'Chamados'

    def __str__(self):
        return self.problema    