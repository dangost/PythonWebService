from application.entities.countries.model import Country


def temp_country():
    temp = Country()
    temp.CountryId = 0
    temp.CountryName = "Name"
    temp.CountryCode = "133"
    temp.NatLangCode = 228
    temp.CurrencyCode = "123"
    return temp

def test_load():
    fetch = (0, "Name", "133", 228, "123")
    obj = Country()
    obj.load(fetch)

    return obj


assert test_load() == temp_country()
