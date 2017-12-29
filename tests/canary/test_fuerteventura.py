import unittest

from requests import Session
from requests_mock import Adapter, ANY
from pkg_resources import resource_string

from reescraper import Fuerteventura, Response


class TestFuerteventura(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.adapter = Adapter()
        self.session.mount('https://', self.adapter)
        self.instance = Fuerteventura(self.session)
        json_data = resource_string("tests.mocks", "canary.txt").decode("UTF-8")
        self.adapter.register_uri(ANY, ANY, text=json_data)

    def test_instance(self):
        self.assertIsInstance(self.instance, Fuerteventura)

    def test_get(self):
        response = self.instance.get()
        self.assertIsInstance(response, Response)
        self.assertIsNotNone(response.timestamp)

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)


if __name__ == '__main__':
    unittest.main()
