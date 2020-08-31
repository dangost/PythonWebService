from application.entities.employmentjobs.model import EmploymentJobs


def temp_employmentjobs():
    temp = EmploymentJobs()
    temp.HRJobId = 0
    temp.CountriesCountryId = 1
    temp.JobTitle = "123"
    temp.MinSalary = 1
    temp.MaxSalary = 22
    #
    return temp

def test_load():
    fetch = (0, 1, "123", 1, 22)
    obj = EmploymentJobs()
    obj.load(fetch)

    return obj


assert test_load() == temp_employmentjobs()
