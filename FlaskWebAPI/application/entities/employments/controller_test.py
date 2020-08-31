import requests
        
json = {"PersonId": 1,
                       "HRJobId":  2,
                       "ManagerEmployeeId": 3,
                       "StartDate":  "today",
                       "EndDate": "next life",
                       "Salary":  123,
                       "CommissionPercent":  100,
                       "Employmentcol": "asdff"}

        
url = "http://127.0.0.1:5000/api/Employments"
        
assert requests.get(url).status_code == 200
        
assert requests.post(url, json=json).status_code == 200
        
assert requests.put(url+'/1', json=json).status_code == 200
        
assert requests.get(url+'/1').status_code == 200
        
assert requests.delete(url+'/1').status_code != 200
    