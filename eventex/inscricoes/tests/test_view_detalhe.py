from django.test import TestCase

from eventex.inscricoes.models import Inscricao


class InscricaoDetalheGet(TestCase):
    def setUp(self):
        self.obj = Inscricao.objects.create(
            name='Luciano Vaz',
            cpf='12345678901',
            email='vazcaino@gmail.com',
            phone='47-984611785'
        )
        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'inscricoes/inscricao_detalhe.html')

    def test_context(self):
        inscricao = self.resp.context['inscricao']
        self.assertIsInstance(inscricao, Inscricao)

    def test_html(self):
        conteudo = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)

        with self.subTest():
            for esperado in conteudo:
                self.assertContains(self.resp, esperado)


class InscricaoDetalheNaoEncontrado(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/0/')

    def test_nao_encontrado(self):
        self.assertEqual(404, self.resp.status_code)