from django.test import TestCase
from model_mommy import mommy
from .models import Logradouro, Cidade


class TesteCidade(TestCase):
    def setUp(self):
        self.cidade = mommy.make(Cidade, cidade="São Paulo", uf="SP")

    def testar(self):
        self.assertTrue(self.cidade.__str__(), Cidade.cidade)


class TesteEndereco(TestCase):
    def setUp(self):
        self.cidade = mommy.make(Cidade, cidade="São Paulo", uf="SP")
        self.endereco = mommy.make(Logradouro, logradouro="Rua Nicia Coutinho", numero="711", cidade=self.cidade)

    def testar(self):
        self.assertTrue(self.endereco.__str__(), Logradouro.logradouro)
