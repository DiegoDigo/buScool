from __future__ import unicode_literals
from django.db import models
from cliente.models import Responsavel
from endereco.models import Logradouro


class Veiculo(models.Model):
    tipoVeiculo = models.CharField(verbose_name="Tipo Veiculo", max_length=100)
    capacidade = models.PositiveIntegerField(default=50)
    capacidadeDeficiente = models.PositiveIntegerField(default=1, null=True, blank=True)
    responsavel = models.ManyToManyField(Responsavel, related_name="responsavel", verbose_name=u'Pais', blank=True)

    class Meta:
        ordering = ['tipoVeiculo']
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'

    def __str__(self):
        return self.tipoVeiculo


class Motorista(models.Model):
    nome = models.CharField(verbose_name=u'Nome', max_length=100)
    apelido = models.CharField(verbose_name=u"Apelido", max_length=100, null=True, blank=True)
    email = models.EmailField(verbose_name=u'E-mail')
    numeroDDD = models.CharField(verbose_name=u'DDD', max_length=5)
    telefone = models.CharField(verbose_name=u'Numero Fixo', max_length=8, null=True, blank=True)
    celular = models.CharField(verbose_name=u'Numero Celular', max_length=9)
    categoria = models.CharField(verbose_name=u'Categoria Habilitação', max_length=2)
    endereco = models.ForeignKey(Logradouro, verbose_name=u'endereco', related_name="endereco")
    criadoEm = models.DateField(auto_now=True, auto_now_add=False)
    descricao = models.TextField(verbose_name=u"Descrição", null=True, blank=True, default="Venha conecer nossos serviços")
    veiculo = models.ForeignKey(Veiculo, related_name="Veiculos", verbose_name=u'Veiculos')
    deficiente = models.BooleanField(verbose_name="Aceita Deficiência", default=False)


    class Meta:
        ordering = ['nome']
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'

    def __str__(self):
        return self.nome
