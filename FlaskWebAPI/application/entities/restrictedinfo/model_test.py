from application.entities.restrictedinfo.model import RestrictedInfo


def temp_restrictedinfo():
    temp = RestrictedInfo()
    temp.PersonId = 1
    temp.DateOfBirth = "qer"
    temp.DateOfDeath = "qw"
    temp.GovernmentId = "asd"
    temp.PassportId = "MP"
    temp.HireDire = "qw"
    temp.SeniorityCode = 12
    #
    return temp

def test_load():
    fetch = (1,"qer", "qw", "asd", "MP", "qw", 12)
    obj = RestrictedInfo()
    obj.load(fetch)

    return obj


assert test_load() == temp_restrictedinfo()
