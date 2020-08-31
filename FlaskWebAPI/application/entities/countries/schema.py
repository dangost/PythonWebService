
def get_json_schema():
    json = {"CountryName": {"type": "string", "minlength": 1},
                    "CountryCode": {"type": "string", "minlength": 1},
                    "NatLangCode": {"type": "integer"},
                    "CurrencyCode": {"type": "string", "minlength": 1}}

    return json
    
    