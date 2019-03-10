import uuid

class Models:

	def __init__(self,incident_id, createdOn, createdBy, location, status, incident_type, images, videos, comment):
		self.incident_id = incident_id
		self.createdOn = createdOn
		self.createdBy = createdBy
		self.location = location
		self.status = status
		self.incident_type = incident_type
		self.images = images
		self.videos = videos
		self.comment = comment