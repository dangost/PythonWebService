from dataclasses import dataclass


@dataclass()
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


	EmployeeId: int

	PersonId: int

	HRJobId: int

	ManagerEmployeeId: int

	StartDate: str

	EndDate: str

	Salary: int

	CommissionPercent: int

	Employmentcol: str