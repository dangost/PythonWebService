from application.entities.customercompanies.model import CustomerCompany


def temp_customercompany():
    temp = CustomerCompany()
    temp.CompanyId = 0
    temp.CompanyName = "qweqwe"
    temp.CompanyCreditLimit = 1233
    temp.CreditLimitCurrency = "euro"
    return temp

def test_load():
    fetch = (0, "qweqwe", 1233, "euro")
    obj = CustomerCompany()
    obj.load(fetch)

    return obj


assert test_load() == temp_customercompany()
