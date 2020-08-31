from application.entities.orders.model import Orders
import application.entities.orders.schema as base
import sqlite3
from typing import List
from application.entities.orders.interface import BaseOrdersRepository


class OrdersRepository(BaseOrdersRepository):
    sqlite_path = "sqlite.db"

    def add(self, obj) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        obj.CustomerId = 1
        obj.OrderId = 1
        request = "INSERT INTO Orders(OrderId, SalesRepId, OrderDate, OrderCode, OrderStatus, OrderTotal, OrderCurrency, PromotionCode) VALUES (\"" + str(
            obj.OrderId) + "\" ,\"" + str(obj.SalesRepId) + "\", \"" + obj.OrderDate + "\", \"" + str(
            obj.OrderCode) + "\", \"" + obj.OrderStatus + "\", \"" + str(
            obj.OrderTotal) + "\", \"" + obj.OrderCurrency + "\", \"" + obj.PromotionCode + "\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM Orders WHERE OrderId = " + str(id) + ";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE Orders SET SalesRepId = " + str(
            obj.SalesRepId) + ",OrderDate = '" + obj.OrderDate + "',OrderCode = " + str(
            obj.OrderCode) + ",OrderStatus = '" + obj.OrderStatus + "',OrderTotal = " + str(
            obj.OrderTotal) + ",OrderCurrency = '" + obj.OrderCurrency + "',PromotionCode = '" + obj.PromotionCode + "' WHERE OrderId= " + str(
            id) + ";"
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
        request = "SELECT * FROM Orders WHERE OrderId = " + str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        orders = Orders()
        orders.load(fetch)
        return orders


    