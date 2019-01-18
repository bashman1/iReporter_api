import unittest
from api import app
from api.views import incident

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.test_incident = {"comment": "This is the Patched comment", \
            "created_by": 3,"created_on": "17/01/2019 12:12","images": "heelo.png", \
            "incident_id": 1,"incident_type": "redflag","location": "kampala",\
            "status": "drafted","videos": "helo.mp4"}
        self.test_incident2 = {"comment": "This is the Patched comment", \
            "created_by": 3,"created_on": "17/01/2019 12:12","images": "heelo.png", \
            "incident_id": 3,"incident_type": "redflag","location": "kampala",\
            "status": "drafted","videos": "helo.mp4"}
        self.test_user =  {"email": "bs@gmail.com","firstname": "bash","is_admin":False,\
            "lastname": "saidi","othername": "gun","phone_number": 1345, \
            "registered": "17/01/2019 16:04","user_id": 5,"username": "bsh"}


    def tearDown(self):
        incident.incident_list, incident.user_list = [],[]

    def test_wlcome_message(self):
        response = self.client.get('v1/api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('welcome to iReporter', str(response.data))

    def test_empty_incidents_list(self):
        response = self.client.get('v1/api/red-flags')
        self.assertEqual(response.status_code, 200)

    def test_empty_user_list(self):
        response = self.client.get('v1/api/users')
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        self.assertEqual(len(incident.fetch_all_users()), 0)
        response = self.client.post('v1/api/users', json = self.test_user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(incident.fetch_all_users()), 1)

    def test_report_incident(self):
        self.assertEqual(len(incident.fetch_all_incidence()), 0)
        response = self.client.post('v1/api/incidents', json =self.test_incident)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(incident.fetch_all_incidence()), 1)


    def test_fetch_specific_incident(self):
        responce = self.client.delete('v1/api/red-flags/1')
        # self.assertEqual(response.status_code, 201)
        self.assertEqual(len(incident.fetch_all_incidence()), 0)

    def test_fetch_specific_incident(self):
        # self.client.post('v1/api/incidents', json =self.test_incident)
        # self.client.post('v1/api/incidents', json =self.test_incident2)
        response = self.client.get('v1/api/red-flags/1')
        self.assertEqual(response.status_code, 200)

