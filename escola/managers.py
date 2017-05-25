from __future__ import unicode_literals
from endereco.models import Logradouro
from django.db import models


class EscolaQuerySet(models.query.QuerySet):

    def escola(self, nome):
        return self.get(nomeEscola=nome)

    def escolasCidade(self, cidade):
        return self.filter(endereco__cidade=cidade)