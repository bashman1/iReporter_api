import unittest
from api import app
from api.views import incident

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.test_incident = {
            "incident": {
                "comment": "this is again a trial",
                "created_on": 1,
                "images": "heelo.png",
                "incident_id": 1,
                "incident_type": "redflag",
                "location": "kampala",
                "status": "drafted",
                "videos": "helo.mp4"
            }
        }
    def tearDown(self):
        incident.incident_list, user_list = [],[]

    def test_wlcome_message(self):
        response = self.client.get('v1/api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('welcome to iReporter', str(response.data))

    def test_empty_incident_list(self):
        response = self.client.get('/v1/api/incidents')
        self.assertEqual(response.status_code, 200)

    def test_report_incidet(self):
        self.assertEqual(len(incident.fetch_all_incidence()), 0)
        response = self.client.post('/v1/api/incidents', json = self.test_report_incidet)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(incident.fetch_all_incidence()), 1)