from django.test import TestCase

# Create your tests here.

class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        ''' GET tem que retornar o código 200 '''
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        ''' O template tem que ser o index.html '''
        self.assertTemplateUsed(self.response, 'index.html')

    def test_link_inscricao(self):
        self.assertContains(self.response, 'href="/inscricao/"')
