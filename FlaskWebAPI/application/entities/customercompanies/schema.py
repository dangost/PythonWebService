
def get_json_schema():
    json = {"CompanyName": {"type": "string", "minlength": 1},
                            "CompanyCreditLimit": {"type": "integer"},
                            "CreditLimitCurrency": {"type": "string", "minlength": 1}}

    return json
    
    