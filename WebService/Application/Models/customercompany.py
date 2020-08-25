from dataclasses import dataclass


@dataclass()
class CustomerCompany:

	def __init__(self):
		pass

	def load(self, fetch):
		self.CompanyId = fetch[0]
		self.CompanyName = fetch[1]
		self.CompanyCreditLimit = fetch[2]
		self.CreditLimitCurrency = fetch[3]


	CompanyId: int

	CompanyName: str

	CompanyCreditLimit: str

	CreditLimitCurrency: str