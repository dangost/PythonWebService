from dataclasses import dataclass


@dataclass()
class PhoneNumber:

	def __init__(self):
		pass

	def load(self, fetch):
		self.PhoneNumberId = fetch[0]
		self.PeoplePersonId = fetch[1]
		self.LocationLocationId = fetch[2]
		self.Phonenumber = fetch[3]
		self.CountryCode = fetch[4]
		self.PhoneType = fetch[5]


	PhoneNumberId: int

	PeoplePersonId: int

	LocationLocationId: int

	Phonenumber: int

	CountryCode: int

	PhoneType: int