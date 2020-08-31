
def get_json_schema():
    json = {"CountryId": {"type": "integer"},
                     "AdressLine1": {"type": "string", "minlength": 1},
                     "AdressLine2":  {"type": "string", "minlength": 1},
                     "City":  {"type": "string", "minlength": 1},
                     "State":  {"type": "string", "minlength": 1},
                     "District":  {"type": "string", "minlength": 1},
                     "PostalCode":  {"type": "string", "minlength": 1},
                     "LocationTypeCode":  {"type": "integer"},
                     "Description": {"type": "string", "minlength": 1},
                     "ShippingNotes":  {"type": "string", "minlength": 1},
                     "CountriesCountryId": {"type": "integer"}}

    return json
    
    