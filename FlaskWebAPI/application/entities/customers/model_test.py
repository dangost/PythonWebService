from application.entities.customers.model import Customer


def temp_customer():
    temp = Customer()

    temp.CustomId = 1
    temp.PersonId = 1
    temp.CustomerEmployeeId = 1
    temp.AccountMgrId = 1
    temp.IncomeLevel = 1
    #
    return temp

def test_load():
    fetch = (1,1,1,1,1)
    obj = Customer()
    obj.load(fetch)

    return obj


assert test_load() == temp_customer()
