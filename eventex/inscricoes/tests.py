from django.core import mail
from django.test import TestCase
from eventex.inscricoes.forms import FormInscricoes

class InscricoesTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/inscricao/')
        self.form = self.resp.context['form']

    def teste_get(self):
        ''' Pegar a url /inscricao/ deve retornar cod 200 '''

        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        ''' Tem que usar o template inscricoes/form_inscricao.html '''

        self.assertTemplateUsed(self.resp, 'inscricoes/form_inscricao.html')

    def test_html(self):
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_tem_form(self):
        self.assertIsInstance(self.form, FormInscricoes)

    def test_tem_campos(self):
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(self.form.fields))


class PostInscricaoTest(TestCase):

    def setUp(self):
        data = dict(name='Luciano Vaz', cpf='12345678901', email='vazcaino@gmail.com', phone='47-98461-1785')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_enviar_email_inscricao(self):
        self.assertEqual(1, len(mail.outbox))

    def test_assunto_email_inscricao(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_origem_email_inscricao(self):
        expect = 'vazcaino@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_corpo_email_inscricao(self):
        self.assertIn('Luciano Vaz', self.email.body)
        self.assertIn('12345678901', self.email.body)
        self.assertIn('vazcaino@gmail.com', self.email.body)
        self.assertIn('47-98461-1785', self.email.body)

class PostInvalidoInscricao(TestCase):

    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})
        self.form = self.resp.context['form']

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'inscricoes/form_inscricao.html')

    def test_tem_form(self):
        self.assertIsInstance(self.form, FormInscricoes)

    def test_form_tem_erros(self):
        self.assertTrue(self.form.errors)

class InscricaoMensagemSucesso(TestCase):

    def test_message(self):
        data = dict(name='Luciano Vaz', cpf='12345678901', email='vazcaino@gmail.com', phone='47-98461-1785')
        response = self.client.post('/inscricao/', data, follow=True)

        self.assertContains(response, 'Inscrição realizada com sucesso!')