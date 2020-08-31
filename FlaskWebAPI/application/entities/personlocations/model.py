from dataclasses import dataclass


@dataclass()
class PersonLocation:

	def __init__(self):
		pass

	def load(self, fetch):
		self.PersonsPersonId = fetch[0]
		self.LocationsLocationsId = fetch[1]
		self.SubAdress = fetch[2]
		self.LocationUsage = fetch[3]
		self.Notes = fetch[4]


	PersonsPersonId: int

	LocationsLocationsId: int

	SubAdress: str

	LocationUsage: str

	Notes: str