from Application.Models.customer import Customer
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists


class CustomersRepository:
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
        request = "INSERT INTO Customers(PersonId, CustomerEmployeeId, AccountMgrId, IncomeLevel) VALUES (\""+str(obj.PersonId)+"\", \""+str(obj.CustomerEmployeeId)+"\", \""+str(obj.AccountMgrId)+"\", \""+str(obj.IncomeLevel)+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM Customers WHERE CustomerId = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj):
        request = "UPDATE Customers SET PersonId = '" + str(obj.PersonId) + "',CustomerEmployeeId = '" + str(obj.CustomerEmployeeId) + "',AccountMgrId = '" + str(obj.AccountMgrId) + "',IncomeLevel = '" + str(obj.IncomeLevel) + " WHERE CustomerId= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT CustomerId, PersonId, CustomerEmployeeId, AccountMgrId, IncomeLevel FROM Customers"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            customer = Customer()
            customer.load(each)
            ls.append(customer.to_json())
        return str(ls)

    def get_id(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM Customers WHERE CustomerId = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        customer = Customer()
        customer.load(fetch)
        return str(customer.to_json())

    