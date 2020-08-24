class CustomerCompany:

	def __init__(self):
		pass

	def load(self, fetch):
		self.CompanyId = fetch[0]
		self.CompanyName = fetch[1]
		self.CompanyCreditLimit = fetch[2]
		self.CreditLimitCurrency = fetch[3]

	def to_json(self):
		dictionary = {"CompanyId": self.CompanyId, "CompanyName": self.CompanyName, "CompanyCreditLimit": self.CompanyCreditLimit, "CreditLimitCurrency": self.CreditLimitCurrency}
		return dictionary


	CompanyId = 0

	CompanyName = ""

	CompanyCreditLimit = ""

	CreditLimitCurrency = ""