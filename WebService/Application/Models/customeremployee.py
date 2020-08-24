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

	def to_json(self):
		dictionary = {"CustomerEmployeeId": self.CustomerEmployeeId, "CompanyId": self.CompanyId, "BadgeNumber": self.BadgeNumber, "JobTitle": self.JobTitle, "Department": self.Department, "CreditLimit": self.CreditLimit, "CreditLimitCurrency": self.CreditLimitCurrency}
		return dictionary


	CustomerEmployeeId = 0

	CompanyId = 0

	BadgeNumber = ""

	JobTitle = ""

	Department = ""

	CreditLimit = 0

	CreditLimitCurrency = 0