import requests
        
json = {"SalesRepId": 1,
                   "OrderDate": "asdf",
                   "OrderCode":  2,
                   "OrderStatus":  "asdf",
                   "OrderTotal":  123,
                   "OrderCurrency":  "asdf",
                   "PromotionCode": "asdfef"}

        
url = "http://127.0.0.1:5000/api/Orders"
        
assert requests.get(url).status_code == 200
        
assert requests.post(url, json=json).status_code == 200
        
assert requests.put(url+'/1', json=json).status_code == 200
        
assert requests.get(url+'/1').status_code == 200
        
assert requests.delete(url+'/1').status_code != 200
    