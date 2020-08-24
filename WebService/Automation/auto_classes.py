class_names = ["Country", "Customer", "CustomerCompany", "CustomerEmployee","Employment","EmploymentJobs","Inventory","Location","OrderItem", "Orders", "Person", "PersonLocation", "PhoneNumber", "Product", "RestrictedInfo", "Warehouse"]
list_names = ["Countries", "Customers", "CustomerCompanies", "CustomerEmployees","Employments", "EmploymentJobs", "Inventories","Locations","OrderItems", "Orders", "People", "PersonLocations","PhoneNumbers", "Products", "RestrictedInfo", "Warehouses"]
id_names = ["CountryId","CustomerId","CompanyId","CustomerEmployeeId","EmployeeID","HRJobId","InventoryId","LocationId","OrderItemId","OrderId","Id","","PhoneNumberId","ProductId","","WarehouseId"]

base = [
    {"CountryId": 'int', "CountryName": "string", "CountryCode": "string", "NatLangCode": "int", "CurrencyCode": "string"},
    {"CustomId": "int", "PersonId": "int", "CustomerEmployeeId": "int", "AccountMgrId": "int", "IncomeLevel": "int"},
    {"CompanyId": "int", "CompanyName": "string", "CompanyCreditLimit": "string", "CreditLimitCurrency": "string"},
    {"CustomerEmployeeId": "int", "CompanyId": "int", "BadgeNumber": "string", "JobTitle": "string", "Department": "string", "CreditLimit": "int", "CreditLimitCurrency": "int"},
    {"EmployeeId": "int", "PersonId": "int","HRJobId": "int", "ManagerEmployeeId": "int", "StartDate": "string", "EndDate": "string", "Salary": "string", "CommissionPercent": "int", "Employmentcol": "string"},
    {"HRJobId": "int", "CountriesCountryId": "int", "JobTitle": "string", "MinSalary": "int", "MaxSalary": "int"},
    {"InventoryId": "int", "ProductId": "int", "WarehouseId": "int", "QuantityOnHand": "int", "QuantityAvaliable": "int"},
    {"LocationId": "int", "CountryId": "int", "AdressLine1": "string", "AdressLine2": "string", "City": "string", "State": "string", "District": "string", "PostalCode": "string", "LocationTypeCode": "int", "Description": "string", "ShippingNotes":"string", "CountriesCountryId": "int"},
    {"OrderItemId": "int", "OrderId": "int", "ProductId":"int", "UnitPrice":"int", "Quantity":"int"},
    {"OrderId":"int", "CustomerId":"int","SalesRepId":"int","OrderDate":"string","OrderCode":"string","OrderStatus":"string", "OrderTotal":"int","OrderCurrency":"string", "PromotionCode":"string"},
    {"Id":"int","FirstName":"string", "LastName":"string", "MiddleName":"string", "Nickname":"string", "NatLangCode":"int", "CultureCode": "int", "Gender":"string"},
    {"PersonsPersonId": "int", "LocationsLocationsId":"int", "SubAdress": "string", "LocationUsage": "string", "Notes": "string"},
    {"PhoneNumberId": "int", "PeoplePersonId":"int", "LocationLocationId": "int", "Phonenumber": "int", "CountryCode": "int", "PhoneType": "int"},
    {"ProductId": "int", "ProductName": "string", "Description": "string", "Category": "int", "WeightClass": "string", "WarrantlyPeriod": "int", "SupplierId": "int", "Status": "string", "ListPrice": "int", "MinimumPrice": "int", "PriceCurrency": "string", "CatalogURL": "string"},
    {"PersonId": "int", "DateOfBirth": "string", "DateOfDeath": "string", "GovernmentId": "string", "PassportId": "string", "HireDire": "string", "SeniorityCode": "int"},
    {"WarehouseId": "int", "LocationId": "int", "WarehouseName": "string"}
]

path = r"D:\Projects\Regula\Web\PythonWebService\WebService\Application\Models"

for i in range(len(class_names)):
    new_path = path + "\\"+class_names[i].lower()+".py"
    file = open(new_path, 'w')

    temp_class = "class " + class_names[i] + ":\n\n"
    temp_class += "\tdef __init__(self):\n\t\tpass\n\n"
    temp_class += "\tdef load(self, fetch):\n"
    load = ""
    fetch = 0
    for each in base[i]:
        load +="\t\tself."+each+" = fetch["+str(fetch)+"]\n"
        fetch += 1
    temp_class += load
    temp_class += "\n\tdef to_json(self):"

    json = ""
    for each in base[i]:
        json += "\""+each+"\": self."+each+", "

    temp_class += "\n\t\tdictionary = {" + json[0:-2] + "}\n\t\treturn dictionary\n"

    props = ""

    for each in base[i]:
        que = None
        if base[i].get(each) == "int":
            que = 0
        else: que = "\"\""

        props += "\n\n\t"+each+" = "+str(que)
    temp_class += props

    file.write(temp_class)


