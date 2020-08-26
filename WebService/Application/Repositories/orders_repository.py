from Application.Models.orders import Orders
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists
from typing import List
from Application.Abstraction.abs_repository import ARepository


class OrdersRepository(Orders, ARepository):
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
        request = "INSERT INTO Orders(SalesRepId, OrderDate, OrderCode, OrderStatus, OrderTotal, OrderCurrency, PromotionCode) VALUES (\""+str(obj.SalesRepId)+"\", \""+obj.OrderDate+"\", \""+str(obj.OrderCode)+"\", \""+obj.OrderStatus+"\", \""+str(obj.OrderTotal)+"\", \""+obj.OrderCurrency+"\", \""+obj.PromotionCode+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM Orders WHERE OrderId = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE Orders SET " + str(obj.SalesRepId) + "',OrderDate = '" + obj.OrderDate + "',OrderCode = '" + str(obj.OrderCode) + "',OrderStatus = '" + obj.OrderStatus + "',OrderTotal = '" + str(obj.OrderTotal) + "',OrderCurrency = '" + obj.OrderCurrency + "',PromotionCode = '" + obj.PromotionCode + " WHERE OrderId= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[Orders]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT OrderId, CustomerId, SalesRepId, OrderDate, OrderCode, OrderStatus, OrderTotal, OrderCurrency, PromotionCode FROM Orders"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            orders = Orders()
            orders.load(each)
            ls.append(orders)
        return ls

    def get_id(self, id) -> Orders:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM Orders WHERE OrderId = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        orders = Orders()
        orders.load(fetch)
        return orders

    