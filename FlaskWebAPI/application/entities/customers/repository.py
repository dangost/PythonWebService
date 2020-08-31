from application.entities.customers.model import Customer
import application.entities.customers.schema as base
import sqlite3
from typing import List
from application.entities.customers.interface import BaseCustomersRepository


class CustomersRepository(BaseCustomersRepository):
    sqlite_path = "sqlite.db"

    def add(self, obj) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "INSERT INTO Customers(CustomerEmployeeId, AccountMgrId, IncomeLevel) VALUES (\"" + str(
            obj.CustomEmployeeId) + "\", \"" + str(obj.AccountMgrId) + "\", \"" + str(obj.IncomeLevel) + "\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM Customers WHERE CustomerId = " + str(id) + ";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE Customers SET CustomerId = " + str(obj.CustomId) + " , CustomerEmployeeId = " + str(
            obj.CustomerEmployeeId) + ",AccountMgrId = " + str(obj.AccountMgrId) + ",IncomeLevel = " + str(
            obj.IncomeLevel) + " WHERE PersonId= " + str(id) + ";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[Customer]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT CustomerId, PersonId, CustomerEmployeeId, AccountMgrId, IncomeLevel FROM Customers"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            customer = Customer()
            customer.load(each)
            ls.append(customer)
        return ls

    def get_id(self, id) -> Customer:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM Customers WHERE PersonId = " + str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        customer = Customer()
        customer.load(fetch)
        return customer


    