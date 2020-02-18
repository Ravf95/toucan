from django.test import TestCase


class AboutTestCase(TestCase):
    url = '/about/'

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
