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

	def to_json(self):
		dictionary = {"Id": self.Id, "FirstName": self.FirstName, "LastName": self.LastName, "MiddleName": self.MiddleName, "Nickname": self.Nickname, "NatLangCode": self.NatLangCode, "CultureCode": self.CultureCode, "Gender": self.Gender}
		return dictionary


	Id = 0

	FirstName = ""

	LastName = ""

	MiddleName = ""

	Nickname = ""

	NatLangCode = 0

	CultureCode = 0

	Gender = ""