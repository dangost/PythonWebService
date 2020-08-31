import requests
        
json = {"CustomerId": 3,
                     "PersonId": 3,
                     "CustomerEmployeeId": 3,
                     "AccountMgrId": 414,
                     "IncomeLevel": 404}

        
url = "http://127.0.0.1:5000/api/Customers"
        
assert requests.get(url).status_code == 200
        
assert requests.post(url, json=json).status_code == 200
        
assert requests.put(url+'/1', json=json).status_code == 200
        
assert requests.get(url+'/1').status_code == 200
        
assert requests.delete(url+'/1').status_code != 200
    