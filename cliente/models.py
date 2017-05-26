
from __future__ import unicode_literals
from django.db import models
from escola.models import Escola
from endereco.models import Logradouro


class Crianca(models.Model):
    nome = models.CharField(verbose_name=u'Nome Filho', max_length=100)
    idade = models.CharField(verbose_name=u'Idade', max_length=3)
    escola = models.ForeignKey(Escola, verbose_name=u'Escola', related_name='escolas')

    class Meta:
        ordering = ['nome']
        verbose_name = u'Criança'
        verbose_name_plural = u'Crianças'

    def __str__(self):
        return self.nome


class Responsavel(models.Model):
    nome = models.CharField(verbose_name=u'Nome', max_length=100)
    email = models.EmailField(verbose_name=u'Email')
    endereco = models.ForeignKey(Logradouro, verbose_name=u"Endereco", related_name="enderecos")
    numeroDDD = models.CharField(verbose_name=u'DDD', max_length=5)
    telefone = models.CharField(verbose_name=u'Numero Fixo', max_length=8, null=True, blank=True)
    celular = models.CharField(verbose_name=u'Numero Celular',max_length=9)
    criadoEm = models.DateField(auto_now=True, auto_now_add=False)
    crianca = models.ManyToManyField(Crianca, verbose_name=u'Filhos', related_name='childrens')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Parents'
        verbose_name_plural = 'Parents'

    def __str__(self):
        return self.nome