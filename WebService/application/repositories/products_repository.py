from application.models.product import Product
import application.base_support.sqlite_support as base
import sqlite3
from os import _exists as file_exists
from typing import List
from application.abstraction.base_repository import BaseRepository


class ProductsRepository(Product, BaseRepository):
    sqlite_path = "sqlite.db"

    def add(self, obj) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "INSERT INTO Products(ProductName, Description, Category, WeightClass, WarrantlyPeriod, SupplierId, Status, ListPrice, MinimumPrice, PriceCurrency, CatalogURL) VALUES (\""+obj.ProductName+"\", \""+obj.Description+"\", \""+str(obj.Category)+"\", \""+str(obj.WeightClass)+"\", \""+str(obj.WarrantlyPeriod)+"\", \""+str(obj.SupplierId)+"\", \""+obj.Status+"\", \""+str(obj.ListPrice)+"\", \""+str(obj.MinimumPrice)+"\", \""+obj.PriceCurrency+"\", \""+obj.CatalogURL+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM Products WHERE ProductId = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE Products SET ProductName = '" + obj.ProductName + "',Description = '" + obj.Description + "',Category = " + str(obj.Category) + ",WeightClass = " + str(obj.WeightClass) + ",WarrantlyPeriod = " + str(obj.WarrantlyPeriod) + ",SupplierId = " + str(obj.SupplierId) + ",Status = '" + obj.Status + "',ListPrice = " + str(obj.ListPrice) + ",MinimumPrice = " + str(obj.MinimumPrice) + ",PriceCurrency = '" + obj.PriceCurrency + "',CatalogURL = '" + obj.CatalogURL + "' WHERE ProductId= "+str(id)+";"
        print(request)
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[Product]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT ProductId, ProductName, Description, Category, WeightClass, WarrantlyPeriod, SupplierId, Status, ListPrice, MinimumPrice, PriceCurrency, CatalogURL FROM Products"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            product = Product()
            product.load(each)
            ls.append(product)
        return ls

    def get_id(self, id) -> Product:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM Products WHERE ProductId = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        product = Product()
        product.load(fetch)
        return product

    