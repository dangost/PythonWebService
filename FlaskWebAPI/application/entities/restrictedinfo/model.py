from dataclasses import dataclass


@dataclass()
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


	PersonId: int

	DateOfBirth: str

	DateOfDeath: str

	GovernmentId: str

	PassportId: str

	HireDire: str

	SeniorityCode: int