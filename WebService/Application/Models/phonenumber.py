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

	def to_json(self):
		dictionary = {"PhoneNumberId": self.PhoneNumberId, "PeoplePersonId": self.PeoplePersonId, "LocationLocationId": self.LocationLocationId, "Phonenumber": self.Phonenumber, "CountryCode": self.CountryCode, "PhoneType": self.PhoneType}
		return dictionary


	PhoneNumberId = 0

	PeoplePersonId = 0

	LocationLocationId = 0

	Phonenumber = 0

	CountryCode = 0

	PhoneType = 0