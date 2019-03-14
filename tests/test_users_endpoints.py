import unittest
from api import app
from api.Users.validators import userlist
import json

class TestUsersEndpoints(unittest.TestCase):

	def setUp(self):
		self.client = app.test_client()

		self.test_user1 =         {
            "email": "tb@gmail.com",
            "firstname": "mugaba",
            "isadmin": False,
            "lastname": "muhamad",
            "othername": "Rashid",
            "password": "123456",
            "phonenumber": "070572621",
            "registered": "110319 2012",
            "user_id": 1,
            "username": "peeep"
            }

		self.test_user2 =         {
            "email": "tb@gmail.com",
            "firstname": "mugaba",
            "isadmin": False,
            "lastname": "muhamad",
            "othername": "Rashid",
            "password": "123456",
            "phonenumber": "070572621",
            "registered": "110319 2012",
            "user_id": 1,
            "username": "peeep"
            }
		self.user_login ={"username": "peeep","password": "123456"}

	def tearDown(self):
		userlist.user_list = []

	def test_welcome_message(self):
		res = self.client.get('/v1/api/',data = json.dumps(self.test_user1),content_type = 'application/json')
		self.assertEqual(res.status_code, 200)
		self.assertIn('Welcome to ireporter', str(res.data))

	def test_signup_a_user(self):
		self.assertEqual(len(userlist.get_all_users()),0)
		res = self.client.post('/v1/api/signUp', 
			data = json.dumps(self.test_user1), 
			content_type = 'application/json')
		self.assertEqual(res.status_code, 201)
		self.assertEqual(len(userlist.get_all_users()),1)
		#self.assertIn('peeep',json.loads(res.data)['message'])

	def test_email_exists_already(self):
		self.test_user1['email']= 'tb@gmail.com'
		self.test_user2['email']= 'tb@gmail.com'
		res = self.client.post('/v1/api/signUp',
			data = json.dumps(self.test_user1),
			content_type = 'application/json')
		res_2 = self.client.post('/v1/api/signUp',
			data = json.dumps(self.test_user2),
			content_type = 'application/json')
		#res_out = json.loads(res.data)
		self.assertEqual(res_2.status_code,400)
		#self.assertIn("email already taken", str(res.data))

	def test_get_all_users(self):
		res = self.client.get('/v1/api/users', 
			data = json.dumps(self.test_user1), 
			content_type = 'application/json')
		self.assertEqual(res.status_code,200)

	def test_empty_username_or_email(self):
		self.test_user1['email'] = ''
		self.test_user1['password'] = ''
		self.test_user1['username'] = ''
		res = self.client.post('/v1/api/signUp',
			data = json.dumps(self.test_user1), 
			content_type = 'application/json')
		#res_out = json.loads(res.data.decode())
		self.assertEqual(res.status_code, 400)
		#self.assertIn('email, username and password cannot be empty',json.loads(res.data)['message'])
	def test_username_exists(self):
		self.test_user1['username']= 'peeep'
		self.test_user2['username']= 'peeep'
		res = self.client.post('/v1/api/signUp',
			data = json.dumps(self.test_user1),
			content_type = 'application/json')
		res_2 = self.client.post('/v1/api/signUp',
			data = json.dumps(self.test_user2),
			content_type = 'application/json')
		self.assertEqual(res_2.status_code, 400)
	def test_login_user(self):
		self.client.post('/v1/api/signUp',
			data = json.dumps(self.test_user1), 
			content_type = 'application/json')
		log_res = self.client.post('/v1/api/login',
			data = json.dumps(self.user_login),
			content_type = 'application/json')
		self.assertEqual(log_res.status_code,200)

	def test_user_empty_name_and_password(self):
		self.user_login['username'] = ''
		self.user_login['password'] = ''
		self.client.post('/v1/api/signUp',
			data = json.dumps(self.test_user1),
			content_type = 'application/json')
		log_res = self.client.post('/v1/api/login',
			data = json.dumps(self.user_login),
			content_type = 'application/json')
		self.assertEqual(log_res.status_code,400)
		self.assertIn('password or username can not be empty',json.loads(log_res.data)['message'])

	def test_username_must_be_string(self):
		self.user_login['username'] = 457
		self.client.post('/v1/api/signUp',
			data = json.dumps(self.test_user1),
			content_type = 'application/json')
		log_res = self.client.post('/v1/api/login',
			data = json.dumps(self.user_login),
			content_type = 'application/json')
		self.assertEqual(log_res.status_code,400)
		self.assertIn('username must be a whole string',json.loads(log_res.data)['message'])

	def test_password_must_string(self):
		self.user_login['password'] = 1223
		self.client.post('/v1/api/signUp',
			data = json.dumps(self.test_user1),
			content_type = 'application/json')
		log_res = self.client.post('/v1/api/login',
			data = json.dumps(self.user_login),
			content_type = 'application/json')
		self.assertEqual(log_res.status_code,400)
		self.assertIn('password must be a string',json.loads(log_res.data)['message'])

	def test_user_doesnot_exist(self):
		self.user_login['username'] = 'pooop'
		self.user_login['password'] = '2345d'
		self.client.post('/v1/api/signUp',
			data = json.dumps(self.test_user1),
			content_type = 'application/json')
		log_res = self.client.post('/v1/api/login',
			data = json.dumps(self.user_login),
			content_type = 'application/json')
		self.assertEqual(log_res.status_code,401)
		self.assertIn('The user doesnot exist',json.loads(log_res.data)['message'])







