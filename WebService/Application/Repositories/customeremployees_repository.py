from Application.Models.customeremployee import CustomerEmployee
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists


class CustomerEmployeesRepository:
    sqlite_path = "sqlite.db"

    def __init__(self):
        self.load()

    def load(self):
        try:
            connection = sqlite3.connect(self.sqlite_path)
            c = connection.cursor()

            for table in Base.CreateBase():
                c.execute(table)

            c.close()
            connection.close()

        except BaseException:
            pass

    def add(self, obj):
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "INSERT INTO CustomerEmployees(CompanyId, BadgeNumber, JobTitle, Department, CreditLimit, CreditLimitCurrency) VALUES (\""+str(obj.CompanyId)+"\", \""+obj.BadgeNumber+"\", \""+obj.JobTitle+"\", \""+obj.Department+"\", \""+str(obj.CreditLimit)+"\", \""+str(obj.CreditLimitCurrency)+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM CustomerEmployees WHERE CustomerEmployeeId = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj):
        request = "UPDATE CustomerEmployees SET CompanyId = '" + str(obj.CompanyId) + "',BadgeNumber = '" + obj.BadgeNumber + "',JobTitle = '" + obj.JobTitle + "',Department = '" + obj.Department + "',CreditLimit = '" + str(obj.CreditLimit) + "',CreditLimitCurrency = '" + str(obj.CreditLimitCurrency) + " WHERE CustomerEmployeeId= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT CustomerEmployeeId, CompanyId, BadgeNumber, JobTitle, Department, CreditLimit, CreditLimitCurrency FROM CustomerEmployees"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            customeremployee = CustomerEmployee()
            customeremployee.load(each)
            ls.append(customeremployee.to_json())
        return str(ls)

    def get_id(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM CustomerEmployees WHERE CustomerEmployeeId = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        customeremployee = CustomerEmployee()
        customeremployee.load(fetch)
        return str(customeremployee.to_json())

    