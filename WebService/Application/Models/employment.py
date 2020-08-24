class Employment:

	def __init__(self):
		pass

	def load(self, fetch):
		self.EmployeeId = fetch[0]
		self.PersonId = fetch[1]
		self.HRJobId = fetch[2]
		self.ManagerEmployeeId = fetch[3]
		self.StartDate = fetch[4]
		self.EndDate = fetch[5]
		self.Salary = fetch[6]
		self.CommissionPercent = fetch[7]
		self.Employmentcol = fetch[8]

	def to_json(self):
		dictionary = {"EmployeeId": self.EmployeeId, "PersonId": self.PersonId, "HRJobId": self.HRJobId, "ManagerEmployeeId": self.ManagerEmployeeId, "StartDate": self.StartDate, "EndDate": self.EndDate, "Salary": self.Salary, "CommissionPercent": self.CommissionPercent, "Employmentcol": self.Employmentcol}
		return dictionary


	EmployeeId = 0

	PersonId = 0

	HRJobId = 0

	ManagerEmployeeId = 0

	StartDate = ""

	EndDate = ""

	Salary = ""

	CommissionPercent = 0

	Employmentcol = ""