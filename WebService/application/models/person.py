from dataclasses import dataclass


@dataclass()
class Person:

	def __init__(self):
		pass

	def load(self, fetch):
		self.Id = fetch[0]
		self.FirstName = fetch[1]
		self.LastName = fetch[2]
		self.MiddleName = fetch[3]
		self.Nickname = fetch[4]
		self.NatLangCode = fetch[5]
		self.CultureCode = fetch[6]
		self.Gender = fetch[7]


	Id: int

	FirstName: str

	LastName: str

	MiddleName: str

	Nickname: str

	NatLangCode: int

	CultureCode: int

	Gender: str