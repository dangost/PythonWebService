from dataclasses import dataclass


@dataclass()
class CustomerEmployee:

	def __init__(self):
		pass

	def load(self, fetch):
		self.CustomerEmployeeId = fetch[0]
		self.CompanyId = fetch[1]
		self.BadgeNumber = fetch[2]
		self.JobTitle = fetch[3]
		self.Department = fetch[4]
		self.CreditLimit = fetch[5]
		self.CreditLimitCurrency = fetch[6]


	CustomerEmployeeId: int

	CompanyId: int

	BadgeNumber: str

	JobTitle: str

	Department: str

	CreditLimit: int

	CreditLimitCurrency: int