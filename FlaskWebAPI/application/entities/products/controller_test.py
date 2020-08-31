import requests
        
json = {"ProductName":  "asd",
                    "Description":  "qwee",
                    "Category":  1332,
                    "WeightClass":  12333,
                    "WarrantlyPeriod": 123,
                    "SupplierId":  14,
                    "Status":  "asdff",
                    "ListPrice": 123,
                    "MinimumPrice":  1233,
                    "PriceCurrency": "asdf",
                    "CatalogURL":  "asdf"}

        
url = "http://127.0.0.1:5000/api/Products"
        
assert requests.get(url).status_code == 200
        
assert requests.post(url, json=json).status_code == 200
        
assert requests.put(url+'/1', json=json).status_code == 200
        
assert requests.get(url+'/1').status_code == 200
        
assert requests.delete(url+'/1').status_code != 200
    