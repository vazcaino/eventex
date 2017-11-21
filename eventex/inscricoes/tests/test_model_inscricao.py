from datetime import datetime
from django.test import TestCase
from eventex.inscricoes.models import Inscricao

class InscricaoModelTest(TestCase):

    def setUp(self):
        self.obj = Inscricao(
            name='Luciano Vaz',
            cpf='12345678901',
            email='vazcaino@gmail.com',
            phone='47-984611785',
        )
        self.obj.save()

    def test_criar(self):
        self.assertTrue(Inscricao.objects.exists())

    def test_criado_em(self):
        """ Inscricao tem que ter um atributo criado_em automaticamente """
        self.assertIsInstance(self.obj.criado_em, datetime)

    def test_str(self):
        self.assertEqual('Luciano Vaz', str(self.obj))

