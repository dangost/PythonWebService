from application.entities.phonenumbers.model import PhoneNumber


def temp_phonenumber():
    temp = PhoneNumber()
    temp.PhoneNumberId = 0
    temp.PeoplePersonId = 1
    temp.LocationLocationId = 1
    temp.Phonenumber = 123131
    temp.CountryCode = 1
    temp.PhoneType = 1
    #
    return temp

def test_load():
    fetch = (0, 1,1,123131,1,1)
    obj = PhoneNumber()
    obj.load(fetch)

    return obj


assert test_load() == temp_phonenumber()
