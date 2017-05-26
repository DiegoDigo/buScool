from django.test import TestCase
from model_mommy import mommy
from .models import Escola
from endereco.models import Cidade, Logradouro


class TesteEscola(TestCase):
    def setUp(self):
        self.cidade = mommy.make(Cidade, cidade="São Paulo", uf="SP")
        self.endereco = mommy.make(Logradouro, logradouro="Rua Nicia Coutinho", numero="711", cidade=self.cidade)
        self.escola = mommy.make(Escola, nomeEscola="Luiza", endereco=self.endereco)

    def testar(self):
        self.assertTrue(self.escola.__str__(), Escola.nomeEscola)
