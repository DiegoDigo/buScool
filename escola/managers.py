from __future__ import unicode_literals
from django.db import models


class EscolaQuerySet(models.query.QuerySet):

    def escola(self, nome):
        return self.get(nomeEscola=nome)

    def escolasCidade(self, cidade):
        return self.filter(endereco__cidade__cidade=cidade)