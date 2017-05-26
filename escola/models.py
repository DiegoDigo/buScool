from __future__ import unicode_literals
from django.db import models
from endereco.models import Logradouro
from .managers import EscolaQuerySet


class Escola(models.Model):
    nomeEscola = models.CharField(verbose_name=u'Nome Escola', max_length=100, unique=True)
    endereco = models.ForeignKey(Logradouro, verbose_name=u"Endereço")
    objects = EscolaQuerySet.as_manager()

    class Meta:
        ordering = ['nomeEscola']
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'

    def __str__(self):
        return self.nomeEscola
