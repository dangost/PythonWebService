from application.entities.warehouses.model import Warehouse
import application.entities.warehouses.schema as base
import sqlite3
from typing import List
from application.entities.warehouses.interface import BaseWarehousesRepository


class WarehousesRepository(BaseWarehousesRepository):
    sqlite_path = "sqlite.db"

    def add(self, obj) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "INSERT INTO Warehouses(LocationId, WarehouseName) VALUES (\"" + str(
            obj.LocationId) + "\", \"" + obj.WarehouseName + "\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM Warehouses WHERE WarehouseId = " + str(id) + ";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE Warehouses SET LocationId = " + str(
            obj.LocationId) + ", WarehouseName = '" + obj.WarehouseName + "' WHERE WarehouseId= " + str(id) + ";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[Warehouse]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT WarehouseId, LocationId, WarehouseName FROM Warehouses"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            warehouse = Warehouse()
            warehouse.load(each)
            ls.append(warehouse)
        return ls

    def get_id(self, id) -> Warehouse:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM Warehouses WHERE WarehouseId = " + str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        warehouse = Warehouse()
        warehouse.load(fetch)
        return warehouse


    