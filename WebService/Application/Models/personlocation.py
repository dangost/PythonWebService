class PersonLocation:

	def __init__(self):
		pass

	def load(self, fetch):
		self.PersonsPersonId = fetch[0]
		self.LocationsLocationsId = fetch[1]
		self.SubAdress = fetch[2]
		self.LocationUsage = fetch[3]
		self.Notes = fetch[4]

	def to_json(self):
		dictionary = {"PersonsPersonId": self.PersonsPersonId, "LocationsLocationsId": self.LocationsLocationsId, "SubAdress": self.SubAdress, "LocationUsage": self.LocationUsage, "Notes": self.Notes}
		return dictionary


	PersonsPersonId = 0

	LocationsLocationsId = 0

	SubAdress = ""

	LocationUsage = ""

	Notes = ""