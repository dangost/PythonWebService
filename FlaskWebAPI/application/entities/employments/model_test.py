from application.entities.employments.model import Employment


def temp_employment():
    temp = Employment()
    temp.EmployeeId = 0
    temp.PersonId = 1
    temp.PersonId = 1
    temp.HRJobId = 1
    temp.ManagerEmployeeId = 1
    temp.StartDate = "1233"
    temp.EndDate = "12313"
    temp.Salary = 123
    temp.CommissionPercent = 3
    temp.Employmentcol = "1233"

    return temp

def test_load():
    fetch = (0, 1,1,1,1, "1233", "12313", 123, 3, "1233")
    obj = Employment()
    obj.load(fetch)

    return obj


assert test_load() == temp_employment()
