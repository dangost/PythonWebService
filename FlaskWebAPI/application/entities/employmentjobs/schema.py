
def get_json_schema():
    json = {"CountriesCountryId": {"type": "integer"},
                       "JobTitle": {"type": "string", "minlength": 1},
                       "MinSalary": {"type": "integer"},
                       "MaxSalary": {"type": "integer"}}

    return json
    
    