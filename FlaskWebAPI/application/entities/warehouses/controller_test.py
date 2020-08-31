import requests
        
json = {"WarehouseId":  1,
                      "LocationId": 2,
                      "WarehouseName": "asdfes"}

        
url = "http://127.0.0.1:5000/api/Warehouses"
        
assert requests.get(url).status_code == 200
        
assert requests.post(url, json=json).status_code == 200
        
assert requests.put(url+'/1', json=json).status_code == 200
        
assert requests.get(url+'/1').status_code == 200
        
assert requests.delete(url+'/1').status_code != 200
    