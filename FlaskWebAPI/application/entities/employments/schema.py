
def get_json_schema():
    json = {"PersonId": {"type": "integer"},
                       "HRJobId":  {"type": "integer"},
                       "ManagerEmployeeId": {"type": "integer"},
                       "StartDate":  {"type": "string", "minlength": 1},
                       "EndDate": {"type": "string", "minlength": 1},
                       "Salary":  {"type": "integer"},
                       "CommissionPercent":  {"type": "integer"},
                       "Employmentcol":  {"type": "string", "minlength": 1}}

    return json
    
    