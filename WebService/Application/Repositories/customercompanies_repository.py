from Application.Models.customercompany import CustomerCompany
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists


class CustomerCompaniesRepository:
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
        request = "INSERT INTO CustomerCompanies(CompanyName, CompanyCreditLimit, CreditLimitCurrency) VALUES (\""+obj.CompanyName+"\", \""+obj.CompanyCreditLimit+"\", \""+obj.CreditLimitCurrency+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM CustomerCompanies WHERE CompanyId = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj):
        request = "UPDATE CustomerCompanies SET CompanyName = '" + obj.CompanyName + "',CompanyCreditLimit = '" + obj.CompanyCreditLimit + "',CreditLimitCurrency = '" + obj.CreditLimitCurrency + " WHERE CompanyId= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT CompanyId, CompanyName, CompanyCreditLimit, CreditLimitCurrency FROM CustomerCompanies"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            customercompany = CustomerCompany()
            customercompany.load(each)
            ls.append(customercompany.to_json())
        return str(ls)

    def get_id(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM CustomerCompanies WHERE CompanyId = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        customercompany = CustomerCompany()
        customercompany.load(fetch)
        return str(customercompany.to_json())

    