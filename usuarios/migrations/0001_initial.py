# Generated by Django 4.0.7 on 2022-10-27 18:40

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=255, verbose_name='Sobrenome')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Nome de usuário')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='E-mail')),
                ('cpf', models.CharField(max_length=255, verbose_name='CPF')),
                ('telefone', models.CharField(max_length=255, verbose_name='Telefone')),
                ('data_nascimento', models.DateField(null=True, verbose_name='Data de Nascimento')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Membro da equipe')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Admin do sistema')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
