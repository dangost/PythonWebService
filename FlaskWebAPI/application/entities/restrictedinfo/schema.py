
def get_json_schema():
    json = {"PersonId":  {"type": "integer"},
                           "DateOfBirth":  {"type": "string", "minlength": 1},
                           "DateOfDeath":  {"type": "string", "minlength": 1},
                           "GovernmentId":  {"type": "string", "minlength": 1},
                           "PassportId":  {"type": "string", "minlength": 1},
                           "HireDire":  {"type": "string", "minlength": 1},
                           "SeniorityCode":  {"type": "integer"}}

    return json
    
    