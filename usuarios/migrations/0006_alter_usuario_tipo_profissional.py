# Generated by Django 4.0.7 on 2022-11-06 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_usuario_tipo_profissional_delete_coordenador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_profissional',
            field=models.CharField(choices=[('1', 'Coordenador de Engenharia Clínica'), ('2', 'Técnico Hospitalar'), ('3', 'Profissional de saúde')], max_length=1),
        ),
    ]