from django.db import models
import uuid

class Equipamento(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    nome = models.CharField(max_length=55, blank=False, null=False)
    numero_serie = models.IntegerField(null=False, blank=False)
    quantidade_falhas = models.IntegerField(default=0, blank=False)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    def __str__(self):
        return self.nome

class Setor(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255, blank=False, null=False)
    quantidade_leitos = models.IntegerField(default=0, blank=False)
    quantidade_profissionais = models.IntegerField(default=0, blank=False)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self):
        return self.nome            