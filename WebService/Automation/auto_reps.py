class_names = ["Country", "Customer", "CustomerCompany", "CustomerEmployee","Employment","EmploymentJobs","Inventory","Location","OrderItem", "Orders", "Person", "PersonLocation", "PhoneNumber", "Product", "RestrictedInfo", "Warehouse"]
list_names = ["Countries", "Customers", "CustomerCompanies", "CustomerEmployees","Employments", "EmploymentJobs", "Inventories","Locations","OrderItems", "Orders", "People", "PersonLocations","PhoneNumbers", "Products", "RestrictedInfo", "Warehouses"]
id_names = ["CountryId","CustomerId","CompanyId","CustomerEmployeeId","EmployeeID","HRJobId","InventoryId","LocationId","OrderItemId","OrderId","Id","","PhoneNumberId","ProductId","","WarehouseId"]

base = [
    {"CountryName": "string", "CountryCode": "string", "NatLangCode": "int", "CurrencyCode": "string"},
    {"PersonId": "int", "CustomerEmployeeId": "int", "AccountMgrId": "int", "IncomeLevel": "int"},
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

path = r"D:\Projects\Regula\Web\PythonWebService\WebService\Application\Repositories"


for i in range(len(class_names)):
    new_path = path + "\\"+list_names[i].lower()+"_repository.py"
    file = open(new_path, 'w')

    t = ""
    #b = '\""+obj.CountryName+"\",\""+obj.CountryCode+"\","+str(obj.NatLangCode)+",\""+obj.CurrencyCode+"\"'
    b = ""
    q = ""
    w = ''
    yes = False
    for each in base[i]:
        if base[i].get(each) == "int":
            t += each + ", "
            b += '\\\""+str(obj.' + each + ')+"\\\", '
            q += each + ", "
            w += '' + each + ' = \'" + str(obj.' + each + ') + "\','
        else:
            t += each + ", "
            b += '\\\""+obj.' + each + '+"\\\", '
            q += each + ", "
            w += '' + each + ' = \'" + obj.' + each + ' + "\','


    insert = "\"INSERT INTO " + list_names[i] + "(" + t[0:-2]+") VALUES ("+b[0:-2]+");\""

    get = "\"SELECT "+id_names[i]+", "+ q[0:-2] + " FROM " + list_names[i] + "\""

    update = "\"UPDATE " + list_names[i] + " SET " + w[0:-2] + " WHERE " + id_names[i] + "= \"+str(id)+\";\""
    #sql = "UPDATE Countries SET CountryName = '" + obj.CountryName + "', CountryCode = '" + obj.CountryCode + "', NatLangCode = " + str(obj.NatLangCode) + ", CurrencyCode = '" + obj.CurrencyCode + "' WHERE CountryId = " + str(id) + ";"


    get_id = "\"SELECT * FROM " + list_names[i] + " WHERE " + id_names[i] + " = \"+str(id)"

    delete = "\"DELETE FROM "+list_names[i]+" WHERE "+id_names[i]+" = \"+str(id)+\";\""

    temp = '''from Application.Models.'''+class_names[i].lower()+''' import '''+class_names[i]+'''
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists
from typing import List
from Application.Abstraction.abs_repository import ARepository


class '''+list_names[i]+'''Repository('''+class_names[i]+''', ARepository):
    sqlite_path = "sqlite.db"

    def __init__(self):
        self.load()

    def load(self) -> None:
        try:
            connection = sqlite3.connect(self.sqlite_path)
            c = connection.cursor()

            for table in Base.CreateBase():
                c.execute(table)

            c.close()
            connection.close()

        except BaseException:
            pass

    def add(self, obj) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = '''+insert+'''
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = '''+delete+'''
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = '''+update+'''
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List['''+class_names[i]+''']:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = '''+get+'''
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            '''+class_names[i].lower()+''' = '''+class_names[i]+'''()
            '''+class_names[i].lower()+'''.load(each)
            ls.append('''+class_names[i].lower()+''')
        return ls

    def get_id(self, id) -> '''+class_names[i]+''':
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = '''+get_id+'''
        cursor.execute(request)
        fetch = cursor.fetchone()
        '''+class_names[i].lower()+''' = '''+class_names[i]+'''()
        '''+class_names[i].lower()+'''.load(fetch)
        return '''+class_names[i].lower()+'''

    '''

    file.write(temp)


