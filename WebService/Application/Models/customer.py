from dataclasses import dataclass


@dataclass()
class Customer:

	def __init__(self):
		pass

	def load(self, fetch):
		self.CustomId = fetch[0]
		self.PersonId = fetch[1]
		self.CustomerEmployeeId = fetch[2]
		self.AccountMgrId = fetch[3]
		self.IncomeLevel = fetch[4]


	CustomId: int

	PersonId: int

	CustomerEmployeeId: int

	AccountMgrId: int

	IncomeLevel: int