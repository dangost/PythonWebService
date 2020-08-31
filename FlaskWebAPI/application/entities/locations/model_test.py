from application.entities.locations.model import Location


def temp_location():
    temp = Location()
    temp.LocationId = 0
    temp.CountryId = 1
    temp.AdressLine1 = "123"
    temp.AdressLine2 = "1233"
    temp.City = "1233"
    temp.State = "1233"
    temp.District = "1231"
    temp.PostalCode = "1233"
    temp.LocationTypeCode = 1244
    temp.Description = "qweqeq"
    temp.ShippingNotes = "1231231fdsjf"
    temp.CountriesCountryId = 1
    #
    return temp

def test_load():
    fetch = (0, 1,"123", "1233", "1233", "1233", "1232", "1233", 1244, "qweqeq", "1231231fdsjf", 1)
    obj = Location()
    obj.load(fetch)

    return obj


assert test_load() == temp_location()
