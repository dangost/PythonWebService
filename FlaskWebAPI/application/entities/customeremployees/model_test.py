from application.entities.customeremployees.model import CustomerEmployee


def temp_customeremployee():
    temp = CustomerEmployee()
    temp.CustomerEmployeeId = 0
    temp.CompanyId = 1
    temp.BadgeNumber = "qeee"
    temp.JobTitle = "qweee"
    temp.Department = "qweeeq"
    temp.CreditLimit = 123
    temp.CreditLimitCurrency = "dolls"
    return temp

def test_load():
    fetch = (0, 1, "qeee", "qweee", "qweeeq", "123", "dolls")
    obj = CustomerEmployee()
    obj.load(fetch)

    return obj


assert test_load() == temp_customeremployee()
