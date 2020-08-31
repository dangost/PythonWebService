
def get_json_schema():
    json = {"CompanyId": {"type": "integer"},
                             "BadgeNumber": {"type": "string", "minlength": 1},
                             "JobTitle": {"type": "string", "minlength": 1},
                             "Department": {"type": "string", "minlength": 1},
                             "CreditLimit": {"type": "integer"},
                             "CreditLimitCurrency": {"type": "string", "minlength": 1}}

    return json
    
    