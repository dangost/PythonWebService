from application.entities.people.model import Person


def temp_person():
    temp = Person()
    temp.PersonId = 0
    temp.FirstName = "1123"
    temp.LastName = "qeq"
    temp.MiddleName = "qwee"
    temp.Nickname = "qwe"
    temp.NatLangCode = 123
    temp.CultureCode = 312
    temp.Gender = "qwe"
    #
    return temp

def test_load():
    fetch = (0, "1123", "qeq", "qwee", "qwe", 123, 312, "qwe")
    obj = Person()
    obj.load(fetch)

    return obj


assert test_load() == temp_person()
