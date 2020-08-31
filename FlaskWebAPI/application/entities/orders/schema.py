
def get_json_schema():
    json = {"SalesRepId": {"type": "integer"},
                   "OrderDate":  {"type": "string", "minlength": 1},
                   "OrderCode":  {"type": "integer"},
                   "OrderStatus":  {"type": "string", "minlength": 1},
                   "OrderTotal":  {"type": "integer"},
                   "OrderCurrency":  {"type": "string", "minlength": 1},
                   "PromotionCode":  {"type": "string", "minlength": 1}}

    return json
    
    