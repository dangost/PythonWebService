class RestrictedInfo:

	def __init__(self):
		pass

	def load(self, fetch):
		self.PersonId = fetch[0]
		self.DateOfBirth = fetch[1]
		self.DateOfDeath = fetch[2]
		self.GovernmentId = fetch[3]
		self.PassportId = fetch[4]
		self.HireDire = fetch[5]
		self.SeniorityCode = fetch[6]

	def to_json(self):
		dictionary = {"PersonId": self.PersonId, "DateOfBirth": self.DateOfBirth, "DateOfDeath": self.DateOfDeath, "GovernmentId": self.GovernmentId, "PassportId": self.PassportId, "HireDire": self.HireDire, "SeniorityCode": self.SeniorityCode}
		return dictionary


	PersonId = 0

	DateOfBirth = ""

	DateOfDeath = ""

	GovernmentId = ""

	PassportId = ""

	HireDire = ""

	SeniorityCode = 0