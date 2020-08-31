import requests
        
json = {"OrderId":  123,
                      "ProductId":  321,
                      "UnitPrice":  124,
                      "Quantity":  1244}

        
url = "http://127.0.0.1:5000/api/OrderItems"
        
assert requests.get(url).status_code == 200
        
assert requests.post(url, json=json).status_code == 200
        
assert requests.put(url+'/1', json=json).status_code == 200
        
assert requests.get(url+'/1').status_code == 200
        
assert requests.delete(url+'/1').status_code != 200
    