from django.core import mail
from django.test import TestCase

class InscricaoPostValido(TestCase):

    def setUp(self):
        data = dict(name='Luciano Vaz', cpf='12345678901', email='vazcaino@gmail.com', phone='47-98461-1785')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_email_inscricao_assunto(self):

        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_email_inscricao_origem(self):

        expect = 'vazcaino@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_email_inscricao_corpo(self):

        conteudos = ['Luciano Vaz',
                     '12345678901',
                     'vazcaino@gmail.com',
                     '47-98461-1785',]

        for conteudo in conteudos:
            with self.subTest():
                self.assertIn(conteudo, self.email.body)