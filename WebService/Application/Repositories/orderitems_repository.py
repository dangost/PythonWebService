from Application.Models.orderitem import OrderItem
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists
from typing import List
from Application.Abstraction.abs_repository import ARepository


class OrderItemsRepository(OrderItem, ARepository):
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
        request = "INSERT INTO OrderItems(OrderId, ProductId, UnitPrice, Quantity) VALUES (\""+str(obj.OrderId)+"\", \""+str(obj.ProductId)+"\", \""+str(obj.UnitPrice)+"\", \""+str(obj.Quantity)+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM OrderItems WHERE OrderItemId = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE OrderItems SET OrderId = " + str(obj.OrderId) + ",ProductId = " + str(obj.ProductId) + ",UnitPrice = " + str(obj.UnitPrice) + ",Quantity = " + str(obj.Quantity) + " WHERE OrderItemId= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[OrderItem]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT OrderItemId, OrderId, ProductId, UnitPrice, Quantity FROM OrderItems"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            orderitem = OrderItem()
            orderitem.load(each)
            ls.append(orderitem)
        return ls

    def get_id(self, id) -> OrderItem:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM OrderItems WHERE OrderItemId = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        orderitem = OrderItem()
        orderitem.load(fetch)
        return orderitem

    