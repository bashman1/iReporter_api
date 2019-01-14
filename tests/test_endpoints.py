import unittest
from api import app
from api.views import incident

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_wlcome_message(self):
        response = self.client.get('v1/api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('welcome to iReporter', str(response.data))