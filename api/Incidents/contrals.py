from flask import jsonify,request,json, abort
from . methods import IncidentList
from . models import Models 
from datetime import datetime

inciden = IncidentList()

def report_an_incident():
	data = request.get_json()
	if not data or not data.get('createdBy') or not data.get('location') \
	or not data.get('status') or not data.get('incident_type') or not data.get('images') \
	or not data.get('videos') or not data.get('comment'):
		abort(400)
		#return jsonify({"message" : "all fields are empty"}),40

	createdBy,location,status,incident_type,images,videos,comment = \
	data.get('createdBy'),data.get('location'),data.get('status'), \
	data.get('incident_type'),data.get('images'),data.get('videos'), \
	data.get('comment')

	incident_id = inciden.generate_incident_id()

	createdOn = date_today = datetime.now().strftime('%d%m%y %H%M')

	new_incident = Models(incident_id, createdOn, createdBy, location, status, incident_type, images, videos, comment)
	if location == "" or createdBy == '':
		return jsonify({"message": "location and createdBy can not be empty"}),400

	inciden.add_an_incident(new_incident)

	return jsonify({"incident" : inciden.incident_list[-1]}),201

def fetch_all_redflags():
	return jsonify({"red-flags" : inciden.get_all_incidents()}),200

def fetch_specific_redflag(redflag_id):
	if not inciden.get_specific_incident(redflag_id):
		return jsonify({"message" : "NO redflag of that id found"}),401

	return jsonify({"incident" : inciden.get_specific_incident(redflag_id)}),200

def edit_location_of_redflag(redflag_id):
	redflag = inciden.get_specific_incident(redflag_id)
	if redflag:
		location = request.get_json()['location']
		new_location = location
		redflag[0]['location'] = new_location
		return jsonify({"Incident" : redflag}),200

	return jsonify({"Error" : "No incident that id"}),401

def edit_comment_of_redflag(redflag_id):
	redflag = inciden.get_specific_incident(redflag_id)
	if redflag:
		comment = request.get_json()['comment']
		new_comment = comment
		redflag[0]['comment'] = new_comment
		return jsonify({"Incident" : redflag}),200

	return jsonify({"Error" : "No incident that id "}),401


def delete_an_incident(id):
	for redflag in inciden.incident_list:
		if redflag['incident_id'] == id:
			inciden.incident_list.remove(redflag),200
			return jsonify({"message": "incident is now now removed"}),200
	return jsonify({"Error": "The incident your looking for is not found"}),401