from flask import Blueprint
from . validators import create_new_user,getall_users,sign_in_user,homepage


userblueprint = Blueprint('api',__name__)
@userblueprint.route('/')
def index():
	return homepage()

@userblueprint.route('/users', methods = ['POST'] )
def create_user():
	return create_new_user()

@userblueprint.route('/users',methods = ['GET'] )
def fetch_all_users():
	return getall_users()

@userblueprint.route('/login',methods = ['POST'])
def login_user():
	return sign_in_user()