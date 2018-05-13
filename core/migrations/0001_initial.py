# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-13 01:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_cliente', models.CharField(max_length=100, verbose_name='Nome do Cliente')),
                ('endereco', models.CharField(blank=True, max_length=100, null=True, verbose_name='Endereço')),
                ('telefone', models.IntegerField(verbose_name='Telefone')),
                ('veiculo', models.CharField(max_length=30, verbose_name='Modelo do Veículo')),
                ('placa', models.CharField(blank=True, max_length=7, null=True, verbose_name='Placa de Veículo')),
                ('cpf_cnpj', models.IntegerField(blank=True, null=True, verbose_name='CPF ou CNPJ')),
                ('inscricao', models.CharField(blank=True, max_length=30, null=True, verbose_name='Inscrição Estadual')),
                ('garantia', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Garantia')),
                ('pagamento', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Condições de Pagamento')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_modificacao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Orcamento',
            },
        ),
        migrations.CreateModel(
            name='Orcamento_Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6)),
                ('quantidade', models.DecimalField(decimal_places=4, max_digits=6)),
                ('desconto', models.DecimalField(blank=True, decimal_places=4, max_digits=6)),
                ('preco_unitario', models.DecimalField(decimal_places=4, max_digits=15)),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='core.Orcamento')),
            ],
            options={
                'db_table': 'Orcamento_Produto',
            },
        ),
    ]
