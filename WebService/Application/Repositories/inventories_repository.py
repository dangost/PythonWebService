from Application.Models.inventory import Inventory
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists
from typing import List
from Application.Abstraction.abs_repository import ARepository


class InventoriesRepository(Inventory, ARepository):
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
        request = "INSERT INTO Inventories(ProductId, WarehouseId, QuantityOnHand, QuantityAvaliable) VALUES (\""+str(obj.ProductId)+"\", \""+str(obj.WarehouseId)+"\", \""+str(obj.QuantityOnHand)+"\", \""+str(obj.QuantityAvaliable)+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM Inventories WHERE InventoryId = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE Inventories SET ProductId = '" + str(obj.ProductId) + "',WarehouseId = '" + str(obj.WarehouseId) + "',QuantityOnHand = '" + str(obj.QuantityOnHand) + "',QuantityAvaliable = '" + str(obj.QuantityAvaliable) + " WHERE InventoryId= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[Inventory]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT InventoryId, ProductId, WarehouseId, QuantityOnHand, QuantityAvaliable FROM Inventories"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            inventory = Inventory()
            inventory.load(each)
            ls.append(inventory)
        return ls

    def get_id(self, id) -> Inventory:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM Inventories WHERE InventoryId = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        inventory = Inventory()
        inventory.load(fetch)
        return inventory

    