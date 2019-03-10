from flask import jsonify, request,json,abort
from . models import User
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from . methods import UserList


userlist = UserList()


def create_new_user():

	data = request.get_json()

	if not data or not data['firstname'] or not data['lastname'] or not data['othername'] \
	or not data['username'] or not data['email'] or not data['password'] or not data['phonenumber'] \
	or not data['registered']:

		abort(400)

	firstname,lastname,othername,username,email,password,phonenumber = \
	data.get('firstname'), data.get('lastname'), \
	data.get('othername'), data.get('username'), \
	data.get('email'), data.get('password'), data.get('phonenumber')



	user_id = userlist.generate_user_id()

	isadmin = False
	registered = date_today = datetime.now().strftime('%d%m%y %H%M')

	new_user  = User(user_id, firstname,lastname,othername,username,email, \
		password,phonenumber,registered,isadmin)

	if email == '' or username == '' or password == '':
		return jsonify({"message" : "email, username and password cannot be empty"}),200

	new_user.password = generate_password_hash(password)

	if new_user.email:
		for usie in userlist.user_list:
			if new_user.email == usie['email']:
				return jsonify({"message" : "email already taken"}),200
	if new_user.username:
		for usie in userlist.user_list:
			if new_user.username == usie['username']:
				return jsonify({"message" : "email already taken"}),200
	userlist.add_a_user(new_user),201
	return jsonify({"user" : userlist.user_list[-1]}),200


def getall_users():
	return jsonify({"users" : userlist.get_all_users()})

def sign_in_user():
	data = request.get_json()

	usernme = data.get('username')

	passcode = data.get('password')

	if usernme == '' or passcode == '':
		return jsonify({"message" : "password or username can not be empty"}),400

	if not type(usernme) == str:
		return jsonify({"message" : "username must be a whole string"}),400

	if not type(passcode) == str:
		return jsonify({"message" : "password must be a string"}),400
	for user in userlist.user_list:
		if user['username'] == usernme and check_password_hash(user['password'],passcode):
			return jsonify({"message" : "your welcome {} your loged in ".format(usernme)}),200
	return jsonify({"message" : "The user doesnot exist"})

def homepage():
	return jsonify({"message" : "Welcome to ireporter"}),200