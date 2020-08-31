
def get_json_schema():
    json = {"WarehouseId":  {"type": "integer"},
                      "LocationId":  {"type": "integer"},
                      "WarehouseName":  {"type": "string", "minlength": 1}}

    return json
    
    