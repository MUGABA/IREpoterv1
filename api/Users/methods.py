from flask import jsonify

from api.Users.models import User


class UserList:

	def __init__(self):

		self.user_list = []

	def add_a_user(self,user):
		new_user = user.__dict__
		self.user_list.append(new_user)

	def get_all_users(self):
		return self.user_list

	def generate_user_id(self):

		if len(self.user_list) == 0:
			return 1
		else:
			return len(self.user_list)  + 1

	def get_specific_user(self, id):
		specific_user = [user for user in self.user_list if user['user_id'] == id]

		try:
			return specific_user

		except:
			return ''