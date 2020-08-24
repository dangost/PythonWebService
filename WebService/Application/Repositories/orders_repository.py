from Application.Models.orders import Orders
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists


class OrdersRepository:
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
        request = "INSERT INTO Orders(CustomerId, SalesRepId, OrderDate, OrderCode, OrderStatus, OrderTotal, OrderCurrency, PromotionCode) VALUES (\""+str(obj.CustomerId)+"\", \""+str(obj.SalesRepId)+"\", \""+obj.OrderDate+"\", \""+obj.OrderCode+"\", \""+obj.OrderStatus+"\", \""+str(obj.OrderTotal)+"\", \""+obj.OrderCurrency+"\", \""+obj.PromotionCode+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM Orders WHERE OrderId = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj):
        request = "UPDATE Orders SET CustomerId = '" + str(obj.CustomerId) + "',SalesRepId = '" + str(obj.SalesRepId) + "',OrderDate = '" + obj.OrderDate + "',OrderCode = '" + obj.OrderCode + "',OrderStatus = '" + obj.OrderStatus + "',OrderTotal = '" + str(obj.OrderTotal) + "',OrderCurrency = '" + obj.OrderCurrency + "',PromotionCode = '" + obj.PromotionCode + " WHERE OrderId= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT OrderId, CustomerId, SalesRepId, OrderDate, OrderCode, OrderStatus, OrderTotal, OrderCurrency, PromotionCode FROM Orders"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            orders = Orders()
            orders.load(each)
            ls.append(orders.to_json())
        return str(ls)

    def get_id(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM Orders WHERE OrderId = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        orders = Orders()
        orders.load(fetch)
        return str(orders.to_json())

    