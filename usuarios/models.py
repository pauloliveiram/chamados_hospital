from tabnanny import verbose
from tkinter import CASCADE
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

class Usuario(AbstractBaseUser, PermissionsMixin):
    PROFISSIONAL_CHOICES = (
        ('1', 'Coordenador de Engenharia Clínica'),
        ('2', 'Técnico Hospitalar'),
        ('3', 'Profissional de saúde')
        )


    nome = models.CharField("Nome", max_length=255, blank=False)
    sobrenome = models.CharField("Sobrenome", max_length=255, blank=False)
    username = models.CharField("Nome de usuário", max_length=255, blank=False, unique=True)
    email = models.EmailField("E-mail", max_length=255, blank=False, unique=True)
    cpf = models.CharField("CPF", max_length=255, blank=False)
    telefone = models.CharField("Telefone", max_length=255, blank=False)
    data_nascimento = models.DateField("Data de Nascimento", null=True)
    tipo_profissional = models.CharField(max_length=1, choices=PROFISSIONAL_CHOICES, blank=False, null=False)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=True)
    is_staff = models.BooleanField('Membro da equipe', default=False)
    is_superuser = models.BooleanField('Admin do sistema', default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nome', 'sobrenome', 'email', 'cpf', 'tipo_profissional']

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
