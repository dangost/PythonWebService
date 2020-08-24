class EmploymentJobs:

	def __init__(self):
		pass

	def load(self, fetch):
		self.HRJobId = fetch[0]
		self.CountriesCountryId = fetch[1]
		self.JobTitle = fetch[2]
		self.MinSalary = fetch[3]
		self.MaxSalary = fetch[4]

	def to_json(self):
		dictionary = {"HRJobId": self.HRJobId, "CountriesCountryId": self.CountriesCountryId, "JobTitle": self.JobTitle, "MinSalary": self.MinSalary, "MaxSalary": self.MaxSalary}
		return dictionary


	HRJobId = 0

	CountriesCountryId = 0

	JobTitle = ""

	MinSalary = 0

	MaxSalary = 0