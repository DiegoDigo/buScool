# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('escola', '0003_auto_20170525_1242'),
        ('endereco', '0002_auto_20170526_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crianca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome Filho')),
                ('idade', models.CharField(max_length=3, verbose_name='Idade')),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escolas', to='escola.Escola', verbose_name='Escola')),
            ],
            options={
                'verbose_name_plural': 'Crianças',
                'ordering': ['nome'],
                'verbose_name': 'Criança',
            },
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('numeroDDD', models.CharField(max_length=5, verbose_name='DDD')),
                ('telefone', models.CharField(blank=True, max_length=8, null=True, verbose_name='Numero Fixo')),
                ('celular', models.CharField(max_length=9, verbose_name='Numero Celular')),
                ('criadoEm', models.DateField(auto_now=True)),
                ('crianca', models.ManyToManyField(related_name='childrens', to='cliente.Crianca', verbose_name='Filhos')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to='endereco.Logradouro', verbose_name='Endereco')),
            ],
            options={
                'verbose_name_plural': 'Parents',
                'ordering': ['nome'],
                'verbose_name': 'Parents',
            },
        ),
    ]
