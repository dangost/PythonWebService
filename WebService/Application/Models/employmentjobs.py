from dataclasses import dataclass


@dataclass()
class EmploymentJobs:

	def __init__(self):
		pass

	def load(self, fetch):
		self.HRJobId = fetch[0]
		self.CountriesCountryId = fetch[1]
		self.JobTitle = fetch[2]
		self.MinSalary = fetch[3]
		self.MaxSalary = fetch[4]


	HRJobId: int

	CountriesCountryId: int

	JobTitle: str

	MinSalary: int

	MaxSalary: int