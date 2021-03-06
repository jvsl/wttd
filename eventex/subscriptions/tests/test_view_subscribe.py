from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm



class SubscribeTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        '''Get /inscricao/ must return status code 200'''

        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='joao', cpf='1234567891',
                    email="ccjoaovictor@gmail.com", phone="23-1234-2323")
        self.resp = self.client.post('/inscricao/', data)
    def test_post(self):
        '''
        :return: valid POST should redirect to /inscricao/
        '''

        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))


class SubscriveInvalidPost(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})

    def test_post(self):
        '''invalid POST should not redirect'''
        self.assertEqual(200, self.resp.status_code )

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)


class SubscribeSuccessMessage(TestCase):

    def test_message(self):
        data_ = dict(name='joao', cpf='12345678911',
                    email="ccjoaovictor@gmail.com", phone="23-1234-2323")
        response = self.client.post('/inscricao/', data_, follow=True)
        self.assertContains(response, 'Inscricao realizada com sucesso')


