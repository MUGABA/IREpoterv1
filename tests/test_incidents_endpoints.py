import json
import unittest
from api import app
from api.Incidents.contrals import inciden



class TestIncidentViews(unittest.TestCase):
	def setUp(self):
		self.client = app.test_client()
		self.incident =  {
        "comment": "a terible car accident happened",
        "createdBy": "2",
        "createdOn": "130319 1122",
        "images": "12.jpeg",
        "incident_id": 1,
        "incident_type": "red-flag",
        "location": "muko",
        "status": "drafted",
        "videos": "helo.mp4"
    }
	def tearDown(self):
		inciden.incident_list = []

	def test_create_an_incident_redflag(self):
		response = self.client.post('/v1/api/incidents',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		self.assertEqual(response.status_code,201)

	def test_empty_location_and_createdby(self):
		self.incident['location'] = ''
		self.incident['createdBy'] = ''
		response = self.client.post('/v1/api/incidents',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		self.assertEqual(response.status_code,400)
		#self.assertIn('location and createdBy can not be empty', json.loads(response.data)['message'])
	def test_get_redglages(self):
		response = self.client.get('/v1/api/red-flags',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		self.assertEqual(response.status_code,200)

	def test_get_specific_redflag(self):
		self.client.post('/v1/api/incidents',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		response = self.client.get('/v1/api/red-flags/1',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		self.assertEqual(response.status_code,200)

	def test_redflag_doesnot_exist(self):
		response = self.client.get('/v1/api/red-flags/1',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		self.assertEqual(response.status_code, 401)
		self.assertIn('NO redflag of that id found',json.loads(response.data)['message'])
	def test_edit_location_of_redflag(self):
		self.incident['location'] = 'jinja'
		self.incident['new_location'] = 'kampala'
		self.client.post('/v1/api/incidents',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		response = self.client.patch('/v1/api/red-flags/1/location',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		self.assertEqual(response.status_code, 200)
	def test_edit_location_of_redflag_not_found(self):
		self.incident['location'] = 'jinja'
		self.incident['new_location'] = 'kampala'
		response = self.client.patch('/v1/api/red-flags/1/location',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		self.assertEqual(response.status_code, 401)
		self.assertIn('No incident that id',json.loads(response.data)['Error'])

	def test_edit_comment_of_redflag(self):
		self.incident['comment'] = 'This accident has been seen at 10 oclock'
		self.incident['new_comment'] = 'The driver has been confirmed dead'
		self.client.post('/v1/api/incidents',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		response = self.client.patch('/v1/api/red-flags/1/comment',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		self.assertEqual(response.status_code, 200)

	def test_edit_comment_of_redflag(self):
		self.incident['comment'] = 'This accident has been seen at 10 oclock'
		self.incident['new_comment'] = 'The driver has been confirmed dead'
		response = self.client.patch('/v1/api/red-flags/1/comment',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		self.assertEqual(response.status_code, 401)
		self.assertIn('No incident that id ', json.loads(response.data)['Error'])
	def test_delete_a_redflag(self):
		self.client.post('/v1/api/incidents',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		response = self.client.delete('/v1/api/red-flags/1',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		self.assertEqual(response.status_code, 200)
		self.assertIn('ncident is now now removed', json.loads(response.data)['message'])
	def test_delete_a_redflag(self):
		response = self.client.delete('/v1/api/red-flags/1',
			data = json.dumps(self.incident),
			content_type = 'application/json')
		self.assertEqual(response.status_code, 401)
		self.assertIn('The incident your looking for is not found', json.loads(response.data)['Error'])



