import requests
        
json = {"CountryId": 12,
                     "AdressLine1": "1asdfff",
                     "AdressLine2":  "asdfdfef",
                     "City":  "asdffef",
                     "State":  "ewrert",
                     "District":  "sdfgfg",
                     "PostalCode":  "sdfefgf",
                     "LocationTypeCode": 4567,
                     "Description": "jfeifjefkdls;a",
                     "ShippingNotes":  "asdjfkl;",
                     "CountriesCountryId": 578}

        
url = "http://127.0.0.1:5000/api/Locations"
        
assert requests.get(url).status_code == 200
        
assert requests.post(url, json=json).status_code == 200
        
assert requests.put(url+'/1', json=json).status_code == 200
        
assert requests.get(url+'/1').status_code == 200
        
assert requests.delete(url+'/1').status_code != 200
    