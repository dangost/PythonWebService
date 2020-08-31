class_names = ["Country", "Customer", "CustomerCompany", "CustomerEmployee", "Employment", "EmploymentJobs",
               "Inventory", "Location", "OrderItem", "Orders", "Person", "PersonLocation", "PhoneNumber", "Product",
               "RestrictedInfo", "Warehouse"]
list_names = ["Countries", "Customers", "CustomerCompanies", "CustomerEmployees", "Employments", "EmploymentJobs",
              "Inventories", "Locations", "OrderItems", "Orders", "People", "PersonLocations", "PhoneNumbers",
              "Products", "RestrictedInfo", "Warehouses"]
id_names = ["CountryId", "CustomerId", "CompanyId", "CustomerEmployeeId", "EmployeeID", "HRJobId", "InventoryId",
            "LocationId", "OrderItemId", "OrderId", "Id", "", "PhoneNumberId", "ProductId", "", "WarehouseId"]

base = [
    {"CountryName": "string", "CountryCode": "string", "NatLangCode": "int", "CurrencyCode": "string"},
    {"PersonId": "int", "CustomEmployeeId": "int", "AccountMgrId": "int", "IncomeLevel": "int"},
    {"CompanyName": "string", "CompanyCreditLimit": "string", "CreditLimitCurrency": "string"},
    {"CompanyId": "int", "BadgeNumber": "string", "JobTitle": "string", "Department": "string", "CreditLimit": "int",
     "CreditLimitCurrency": "int"},
    {"PersonId": "int", "HRJobId": "int", "ManagerEmployeeId": "int", "StartDate": "string", "EndDate": "string",
     "Salary": "string", "CommissionPercent": "int", "Employmentcol": "string"},
    {"CountriesCountryId": "int", "JobTitle": "string", "MinSalary": "int", "MaxSalary": "int"},
    {"ProductId": "int", "WarehouseId": "int", "QuantityOnHand": "int", "QuantityAvaliable": "int"},
    {"CountryId": "int", "AdressLine1": "string", "AdressLine2": "string", "City": "string", "State": "string",
     "District": "string", "PostalCode": "string", "LocationTypeCode": "int", "Description": "string",
     "ShippingNotes": "string", "CountriesCountryId": "int"},
    {"OrderId": "int", "ProductId": "int", "UnitPrice": "int", "Quantity": "int"},
    {"CustomerId": "int", "SalesRepId": "int", "OrderDate": "string", "OrderCode": "string", "OrderStatus": "string",
     "OrderTotal": "int", "OrderCurrency": "string", "PromotionCode": "string"},
    {"FirstName": "string", "LastName": "string", "MiddleName": "string", "Nickname": "string", "NatLangCode": "int",
     "CultureCode": "int", "Gender": "string"},
    {"LocationsLocationsId": "int", "SubAdress": "string", "LocationUsage": "string", "Notes": "string"},
    {"PeoplePersonId": "int", "LocationLocationId": "int", "Phonenumber": "int", "CountryCode": "int",
     "PhoneType": "int"},
    {"ProductName": "string", "Description": "string", "Category": "int", "WeightClass": "string",
     "WarrantlyPeriod": "int", "SupplierId": "int", "Status": "string", "ListPrice": "int", "MinimumPrice": "int",
     "PriceCurrency": "string", "CatalogURL": "string"},
    {"DateOfBirth": "string", "DateOfDeath": "string", "GovernmentId": "string", "PassportId": "string",
     "HireDire": "string", "SeniorityCode": "int"},
    {"LocationId": "int", "WarehouseName": "string"}
]

path = r"D:\Projects\Regula\Web\PythonWebService\FlaskWebAPI\application\entities"

for i in range(len(class_names)):
    new_path = path + "\\" + list_names[i].lower() + "\\controller_test.py"
    file = open(new_path, 'w')
    # obj.CountryName = req_data["CountryName"]

    t = ""
    v = "    ls = ["

    temp = '''import requests
        
json = {}
        
url = "http://127.0.0.1:5000/api/'''+list_names[i]+'''"
        
assert requests.get(url).status_code == 200
        
assert requests.post(url, json=json).status_code == 200
        
assert requests.put(url+'/1', json=json).status_code == 200
        
assert requests.get(url+'/1').status_code == 200
        
assert requests.delete(url+'/1').status_code != 200
    '''
    file.write(temp)