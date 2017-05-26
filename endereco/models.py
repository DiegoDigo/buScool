from __future__ import unicode_literals
from django.db import models


class Cidade(models.Model):
    cidade = models.CharField(verbose_name=u"Cidade", max_length=100)
    uf = models.CharField(verbose_name=u"Estado", max_length=2)

    def __str__(self):
        return self.cidade

    class Meta:
        ordering = ['cidade']
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Logradouro(models.Model):
    logradouro = models.CharField(verbose_name=u'Logradouro', max_length=100)
    numero = models.CharField(verbose_name=u'Logradouro Numero', max_length=5)
    cidade = models.ForeignKey(Cidade, verbose_name="Cidade",related_name="cidades")

    def __str__(self):
        return self.logradouro

    class Meta:
        ordering = ['logradouro']
        verbose_name = "Logradouro"
        verbose_name_plural = "Logradouros"

