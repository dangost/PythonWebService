class_names = ["Country", "Customer", "CustomerCompany", "CustomerEmployee","Employment","EmploymentJobs","Inventory","Location","OrderItem", "Orders", "Person", "PersonLocation", "PhoneNumber", "Product", "RestrictedInfo", "Warehouse"]
list_names = ["Countries", "Customers", "CustomerCompanies", "CustomerEmployees","Employments", "EmploymentJobs", "Inventories","Locations","OrderItems", "Orders", "People", "PersonLocations","PhoneNumbers", "Products", "RestrictedInfo", "Warehouses"]
id_names = ["CountryId","CustomerId","CompanyId","CustomerEmployeeId","EmployeeID","HRJobId","InventoryId","LocationId","OrderItemId","OrderId","Id","","PhoneNumberId","ProductId","","WarehouseId"]

base = [
    {"CountryName": "string", "CountryCode": "string", "NatLangCode": "int", "CurrencyCode": "string"},
    {"PersonId": "int", "CustomEmployeeId": "int", "AccountMgrId": "int", "IncomeLevel": "int"},
    {"CompanyName": "string", "CompanyCreditLimit": "string", "CreditLimitCurrency": "string"},
    {"CompanyId": "int", "BadgeNumber": "string", "JobTitle": "string", "Department": "string", "CreditLimit": "int", "CreditLimitCurrency": "int"},
    {"PersonId": "int","HRJobId": "int", "ManagerEmployeeId": "int", "StartDate": "string", "EndDate": "string", "Salary": "string", "CommissionPercent": "int", "Employmentcol": "string"},
    {"CountriesCountryId": "int", "JobTitle": "string", "MinSalary": "int", "MaxSalary": "int"},
    {"ProductId": "int", "WarehouseId": "int", "QuantityOnHand": "int", "QuantityAvaliable": "int"},
    {"CountryId": "int", "AdressLine1": "string", "AdressLine2": "string", "City": "string", "State": "string", "District": "string", "PostalCode": "string", "LocationTypeCode": "int", "Description": "string", "ShippingNotes":"string", "CountriesCountryId": "int"},
    {"OrderId": "int", "ProductId":"int", "UnitPrice":"int", "Quantity":"int"},
    {"CustomerId":"int","SalesRepId":"int","OrderDate":"string","OrderCode":"string","OrderStatus":"string", "OrderTotal":"int","OrderCurrency":"string", "PromotionCode":"string"},
    {"FirstName":"string", "LastName":"string", "MiddleName":"string", "Nickname":"string", "NatLangCode":"int", "CultureCode": "int", "Gender":"string"},
    {"LocationsLocationsId":"int", "SubAdress": "string", "LocationUsage": "string", "Notes": "string"},
    {"PeoplePersonId":"int", "LocationLocationId": "int", "Phonenumber": "int", "CountryCode": "int", "PhoneType": "int"},
    {"ProductName": "string", "Description": "string", "Category": "int", "WeightClass": "string", "WarrantlyPeriod": "int", "SupplierId": "int", "Status": "string", "ListPrice": "int", "MinimumPrice": "int", "PriceCurrency": "string", "CatalogURL": "string"},
    {"DateOfBirth": "string", "DateOfDeath": "string", "GovernmentId": "string", "PassportId": "string", "HireDire": "string", "SeniorityCode": "int"},
    {"LocationId": "int", "WarehouseName": "string"}
]

path = r"D:\Projects\Regula\Web\PythonWebService\WebService\Application\Controllers"


for i in range(len(class_names)):
    new_path = path + "\\"+list_names[i].lower()+"_controller.py"
    file = open(new_path, 'w')
    #obj.CountryName = req_data["CountryName"]

    t = ""
    v = "    ls = ["
    for each in base[i]:
        t +="        obj."+each+" = req_data[\""+each+"\"]\n"
        v += "obj."+each+", "

    inv = "    if not validation(ls): return \"Invalid data\""
    v = v[0:-2] +"]\n" +inv

    temp = '''from Application.DI import '''+list_names[i].lower()+'''_db
from flask import jsonify
from flask import Blueprint, request
from Application.BaseSupport.validation import validation
from Application.Repositories.'''+list_names[i].lower()+'''_repository import '''+list_names[i]+'''Repository
from Application.Models.'''+class_names[i].lower()+''' import '''+class_names[i]+'''

'''+list_names[i].lower()+'''_controller_api = Blueprint(\''''+list_names[i].lower()+'''_controller_api\', __name__)

'''+list_names[i].lower()+'''_api = Blueprint(\''''+list_names[i].lower()+'''_api\', __name__)


@'''+list_names[i].lower()+'''_controller_api.route("/api/'''+list_names[i]+'''", methods=['GET'])
def get_'''+list_names[i].lower()+'''():
    return jsonify('''+list_names[i].lower()+'''_db.get())


@'''+list_names[i].lower()+'''_controller_api.route("/api/'''+list_names[i]+'''/<int:id>", methods=['GET'])
def get_'''+list_names[i].lower()+'''_id(id):
    return jsonify('''+list_names[i].lower()+'''_db.get_id(id))


@'''+list_names[i].lower()+'''_controller_api.route("/api/'''+list_names[i]+'''", methods=['POST'])
def post_'''+class_names[i].lower()+'''():
    obj = '''+class_names[i]+'''()
    req_data = request.get_json()
    try:
'''+t+'''
    except BaseException:
        return "Invalid data"
'''+v+'''


    try:
        '''+list_names[i].lower()+'''_db.add(obj)
    except BaseException:
        return "Bad Request!"
    return "OK"


@'''+list_names[i].lower()+'''_controller_api.route("/api/'''+list_names[i]+'''/<int:id>", methods=['DELETE'])
def delete_'''+class_names[i].lower()+'''(id):
    try:
        '''+list_names[i].lower()+'''_db.delete(id)
    except BaseException:
        return "Bad Request!"
    return "OK"


@'''+list_names[i].lower()+'''_controller_api.route("/api/'''+list_names[i]+'''/<int:id>", methods=['PUT'])
def put_'''+class_names[i].lower()+'''(id):
    obj = '''+class_names[i]+'''()
    req_data = request.get_json()
    try:
'''+t+'''
    except BaseException:
        return "Invalid data"
'''+v+'''
    try:
        '''+list_names[i].lower()+'''_db.edit(id, obj)
    except BaseException:
        return "Bad Request!"
    return "OK"

    '''

    file.write(temp)
