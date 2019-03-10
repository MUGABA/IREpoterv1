from flask import Blueprint
from . contrals import report_an_incident,fetch_all_redflags,fetch_specific_redflag, \
edit_location_of_redflag,edit_comment_of_redflag,delete_an_incident

from . methods import IncidentList

incidentbluerprint = Blueprint('app',__name__)

@incidentbluerprint.route('/incidents',methods = ['POST'])
def create_incident():
	return report_an_incident()

@incidentbluerprint.route('/red-flags', methods = ['GET'])
def get_all_redflags():
	return fetch_all_redflags()

@incidentbluerprint.route('/red-flags/<int:redflag_id>', methods = ['GET'])
def get_specific_redflag(redflag_id):
	return fetch_specific_redflag(redflag_id)

@incidentbluerprint.route('/red-flags/<int:redflag_id>/location', methods = ['PATCH'])
def patch_location_of_incident(redflag_id):
	return edit_location_of_redflag(redflag_id)

@incidentbluerprint.route('/red-flags/<int:redflag_id>/comment', methods = ['PATCH'])
def patch_comment_of_incident(redflag_id):
	return edit_comment_of_redflag(redflag_id)

@incidentbluerprint.route('/red-flags/<int:redflag_id>', methods = ['DELETE'])
def remove_an_incident(redflag_id):
	return delete_an_incident(redflag_id)