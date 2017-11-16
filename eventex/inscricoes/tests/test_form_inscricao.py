from django.test import TestCase
from eventex.inscricoes.forms import FormInscricoes


class FormInscricaoTest(TestCase):

    def setUp(self):
        self.form = FormInscricoes()

    def test_tem_campos(self):
        ''' Tem que ter 4 campos '''
        esperado = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(esperado, list(self.form.fields))