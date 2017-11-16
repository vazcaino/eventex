from django.core import mail
from django.test import TestCase
from eventex.inscricoes.forms import FormInscricoes

class InscricaoGet(TestCase):

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
        ''' O Html tem que conter as tags corretas '''
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))

        for texto, cont in tags:
            with self.subTest():
                self.assertContains(self.resp, texto, cont)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_tem_form(self):
        self.assertIsInstance(self.form, FormInscricoes)


class InscricaoPostValido(TestCase):

    def setUp(self):
        data = dict(name='Luciano Vaz', cpf='12345678901', email='vazcaino@gmail.com', phone='47-98461-1785')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_email_inscricao_enviar(self):
        self.assertEqual(1, len(mail.outbox))


class InscricaoPostInvalido(TestCase):

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