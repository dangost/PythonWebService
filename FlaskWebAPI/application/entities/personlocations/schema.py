
def get_json_schema():
    json = {"PersonsPersonId":  {"type": "integer"},
                           "LocationsLocationsId":  {"type": "integer"},
                           "SubAdress": {"type": "string", "minlength": 1},
                           "LocationUsage":  {"type": "string", "minlength": 1},
                           "Notes":  {"type": "string", "minlength": 1}}

    return json
    
    