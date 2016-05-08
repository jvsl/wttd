from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='joao', cpf='1234567891',
                    email="ccjoaovictor@gmail.com", phone="23-1234-2323")
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = "Confirmação de inscrição"
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = "contato@eventex.com.br"
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'ccjoaovictor@gmail.com']

        self.assertEqual(expect, self.email.to)


    def test_subscription_email_body(self):
        contents = ['joao',
                    '1234567891',
                    'ccjoaovictor@gmail.com',
                    '23-1234-2323']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)