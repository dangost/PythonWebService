from Application.Models.product import Product
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists


class ProductsRepository:
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
        request = "INSERT INTO Products(ProductName, Description, Category, WeightClass, WarrantlyPeriod, SupplierId, Status, ListPrice, MinimumPrice, PriceCurrency, CatalogURL) VALUES (\""+obj.ProductName+"\", \""+obj.Description+"\", \""+str(obj.Category)+"\", \""+obj.WeightClass+"\", \""+str(obj.WarrantlyPeriod)+"\", \""+str(obj.SupplierId)+"\", \""+obj.Status+"\", \""+str(obj.ListPrice)+"\", \""+str(obj.MinimumPrice)+"\", \""+obj.PriceCurrency+"\", \""+obj.CatalogURL+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM Products WHERE ProductId = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj):
        request = "UPDATE Products SET ProductName = '" + obj.ProductName + "',Description = '" + obj.Description + "',Category = '" + str(obj.Category) + "',WeightClass = '" + obj.WeightClass + "',WarrantlyPeriod = '" + str(obj.WarrantlyPeriod) + "',SupplierId = '" + str(obj.SupplierId) + "',Status = '" + obj.Status + "',ListPrice = '" + str(obj.ListPrice) + "',MinimumPrice = '" + str(obj.MinimumPrice) + "',PriceCurrency = '" + obj.PriceCurrency + "',CatalogURL = '" + obj.CatalogURL + " WHERE ProductId= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT ProductId, ProductName, Description, Category, WeightClass, WarrantlyPeriod, SupplierId, Status, ListPrice, MinimumPrice, PriceCurrency, CatalogURL FROM Products"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            product = Product()
            product.load(each)
            ls.append(product.to_json())
        return str(ls)

    def get_id(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM Products WHERE ProductId = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        product = Product()
        product.load(fetch)
        return str(product.to_json())

    