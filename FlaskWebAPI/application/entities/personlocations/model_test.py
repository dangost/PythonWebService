from application.entities.personlocations.model import PersonLocation


def temp_personlocation():
    temp = PersonLocation()
    temp.PersonsPersonId = 1
    temp.LocationsLocationsId = 1
    temp.SubAdress = "qweq"
    temp.LocationUsage = "11122"
    temp.Notes = "qweq"
    #
    return temp

def test_load():
    fetch = (1, 1, "qweq", "11122", "qweq")
    obj = PersonLocation()
    obj.load(fetch)

    return obj


assert test_load() == temp_personlocation()
