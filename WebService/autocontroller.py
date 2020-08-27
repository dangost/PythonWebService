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

path = r"D:\Projects\Regula\Web\PythonWebService\WebService\application\controllers"

for i in range(len(class_names)):
    new_path = path + "\\" + list_names[i].lower() + "_controller.py"
    file = open(new_path, 'w')
    # obj.CountryName = req_data["CountryName"]

    t = ""
    v = "    ls = ["
    for each in base[i]:
        t += "        obj." + each + " = req_data[\"" + each + "\"]\n"
        v += "obj." + each + ", "

    inv = "    if not validation(ls): return \"Invalid data\""
    v = v[0:-2] + "]\n" + inv

    temp = '''import json\nimport sqlite3
from application.app import ''' + list_names[i].lower() + '''_db
from http import HTTPStatus
from flask import jsonify
from flask import Blueprint, request
import cerberus
from application.valid.json_schemes import Schemes
from application.models.''' + class_names[i].lower() + ''' import ''' + class_names[i] + '''


''' + list_names[i].lower() + '''_controller_api = Blueprint(\'''' + list_names[i].lower() + '''_controller_api\', __name__)
''' + list_names[i].lower() + '''_api = Blueprint(\'''' + list_names[i].lower() + '''_api\', __name__)


@''' + list_names[i].lower() + '''_controller_api.route("/api/''' + list_names[i] + '''", methods=['GET'])
def get_''' + list_names[i].lower() + '''():
    obj = ''' + list_names[i].lower() + '''_db.get()
    return jsonify(obj), HTTPStatus.OK
    
@''' + list_names[i].lower() + '''_controller_api.route("/api/''' + list_names[i] + '''/<int:id>", methods=['GET'])
def get_''' + list_names[i].lower() + '''_id(id):
    obj = ''' + list_names[i].lower() + '''_db.get_id(id)
    return jsonify(obj), HTTPStatus.OK
    
@''' + list_names[i].lower() + '''_controller_api.route("/api/''' + list_names[i] + '''", methods=['POST'])
def post_''' + class_names[i].lower() + '''():
    obj = ''' + class_names[i] + '''()
    req_data = request.get_json()

    schema = Schemes.''' + class_names[i].lower() + '''_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.NO_CONTENT

    try:
''' + t + '''
    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.NO_CONTENT
    try:
        ''' + list_names[i].lower() + '''_db.add(obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    
@''' + list_names[i].lower() + '''_controller_api.route("/api/''' + list_names[i] + '''/<int:id>", methods=['DELETE'])
def delete_''' + class_names[i].lower() + '''(id):
    try:
        ''' + list_names[i].lower() + '''_db.delete(id)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    
@''' + list_names[i].lower() + '''_controller_api.route("/api/''' + list_names[i] + '''/<int:id>", methods=['PUT'])
def put_''' + class_names[i].lower() + '''(id):
    obj = ''' + class_names[i] + '''()
    req_data = request.get_json()

    schema = Schemes.''' + class_names[i].lower() + '''_json
    v = cerberus.Validator(schema)
    if not v.validate(req_data):
        return "Invalid json", HTTPStatus.NO_CONTENT

    try:
''' + t + '''
    except json.JSONDecodeError:
        return "Invalid data", HTTPStatus.NO_CONTENT
    try:
        ''' + list_names[i].lower() + '''_db.edit(id, obj)
    except sqlite3.DatabaseError:
        return "Bad request", HTTPStatus.BAD_REQUEST
    return "OK", HTTPStatus.OK
    '''

    file.write(temp)