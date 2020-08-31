
def get_json_schema():
    json = {"FirstName":  {"type": "string", "minlength": 1},
                   "LastName":  {"type": "string", "minlength": 1},
                   "MiddleName":  {"type": "string", "minlength": 1},
                   "Nickname":  {"type": "string", "minlength": 1},
                   "NatLangCode":  {"type": "integer"},
                   "CultureCode":  {"type": "integer"},
                   "Gender":  {"type": "string", "minlength": 1}}

    return json
    
    