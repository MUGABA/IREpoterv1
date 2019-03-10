from . models import Models

class IncidentList:

	def __init__(self):
		self.incident_list = []

	def add_an_incident(self,incident):
		new_incident = incident.__dict__
		self.incident_list.append(new_incident)

	def get_all_incidents(self):
		return self.incident_list

	def generate_incident_id(self):

		if len(self.incident_list) == 0:
			return 1
		else:
			return len(self.incident_list)  + 1

	def get_specific_incident(self, id):

		specific_incident = [incident for incident in self.incident_list if incident['incident_id'] == id]

		try:
			return specific_incident

		except:
			return ''