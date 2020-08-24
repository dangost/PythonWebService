class Customer:

	def __init__(self):
		pass

	def load(self, fetch):
		self.CustomId = fetch[0]
		self.PersonId = fetch[1]
		self.CustomerEmployeeId = fetch[2]
		self.AccountMgrId = fetch[3]
		self.IncomeLevel = fetch[4]

	def to_json(self):
		dictionary = {"CustomId": self.CustomId, "PersonId": self.PersonId, "CustomerEmployeeId": self.CustomerEmployeeId, "AccountMgrId": self.AccountMgrId, "IncomeLevel": self.IncomeLevel}
		return dictionary


	CustomId = 0

	PersonId = 0

	CustomerEmployeeId = 0

	AccountMgrId = 0

	IncomeLevel = 0