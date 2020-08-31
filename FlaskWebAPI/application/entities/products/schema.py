
def get_json_schema():
    json = {"ProductName":  {"type": "string", "minlength": 1},
                    "Description":  {"type": "string", "minlength": 1},
                    "Category":  {"type": "integer"},
                    "WeightClass":  {"type": "integer"},
                    "WarrantlyPeriod":  {"type": "integer"},
                    "SupplierId":  {"type": "integer"},
                    "Status":  {"type": "string", "minlength": 1},
                    "ListPrice":  {"type": "integer"},
                    "MinimumPrice":  {"type": "integer"},
                    "PriceCurrency":  {"type": "string", "minlength": 1},
                    "CatalogURL":  {"type": "string", "minlength": 1}}

    return json
    
    