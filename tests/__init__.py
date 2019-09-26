import json
import os.path
from datetime import date
from io import BytesIO
from zipfile import ZipFile

from django.test import TestCase


def path(filename):
    return os.path.join('tests', 'fixtures', filename)


def read(filename, mode='rt', encoding=None, **kwargs):
    with open(path(filename), mode, encoding=encoding, **kwargs) as f:
        return f.read()


class ViewTestCase(TestCase):
    maxDiff = None

    def upload_and_go(self, data=None):
        if data is None:
            data = {}

        for file in self.files:
            with open(path(file)) as f:
                response = self.client.post('/upload/', {'file': f})

        response = self.client.get(self.url + 'go/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

        content = json.loads(response.content.decode('utf-8'))
        return content


class ViewTests:
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')

    def test_go_with_files(self):
        content = self.upload_and_go()

        self.assertEqual(len(content), 2)
        self.assertIsInstance(content['size'], int)
        self.assertRegex(content['url'], r'^/result/' + '{:%Y-%m-%d}'.format(date.today()) + r'/[0-9a-f-]{36}/$')

        if getattr(self, 'result', None):
            response = self.client.get(content['url'])
            zipfile = ZipFile(BytesIO(response.getvalue()))
            names = zipfile.namelist()
            self.assertEqual(names, ['result.json'])
            self.assertEqual(zipfile.read(names[0]).decode('utf-8'), read(self.result))

    def test_go_without_files(self):
        response = self.client.get(self.url + 'go/')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.reason_phrase, 'No files available for operation')
        self.assertEqual(response['Content-Type'], 'application/json')

        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(content, {
            'error': 'No files uploaded',
        })


class PublishedDateTests:
    def test_go_with_valid_published_date(self):
        content = self.upload_and_go({'publishedDate': '2001-02-03T00:00:00Z'})

        self.assertEqual(len(content), 2)
        self.assertIsInstance(content['size'], int)
        self.assertRegex(content['url'], r'^/result/' + '{:%Y-%m-%d}'.format(date.today()) + r'/[0-9a-f-]{36}/$')

    def test_go_with_invalid_published_date(self):
        content = self.upload_and_go({'publishedDate': '2000-00-00T00:00:00Z'})

        self.assertEqual(len(content), 2)
        self.assertIsInstance(content['size'], int)
        self.assertRegex(content['url'], r'^/result/' + '{:%Y-%m-%d}'.format(date.today()) + r'/[0-9a-f-]{36}/$')
