from __future__ import unicode_literals
from django.db import models


class Logradouro(models.Model):
    numero = models.CharField(verbose_name=u'Logradouro Numero', max_length=5)
    logradouro = models.CharField(verbose_name=u'Logradouro', max_length=100)
    cidade = models.CharField(verbose_name=u"Cidade", max_length=100)
    uf = models.CharField(verbose_name=u"Estado", max_length=2)

    def __str__(self):
        return self.cidade

    class Meta:
        ordering = ['cidade']
        verbose_name = "Logradouro"
        verbose_name_plural = "Logradouros"