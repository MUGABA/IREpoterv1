import uuid

class User:

	def __init__(self, user_id , firstname, lastname, othername, \
		username, email, password, phonenumber, registered, isadmin):
		self.user_id = user_id
		self.firstname = firstname
		self.lastname = lastname
		self.othername = othername
		self.username = username
		self.email = email 
		self.password = password
		self.phonenumber = phonenumber
		self.registered = registered
		self.isadmin = isadmin