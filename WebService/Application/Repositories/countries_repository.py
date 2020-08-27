from Application.Models.country import Country
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from typing import List
from Application.Abstraction.abs_repository import ARepository


class CountriesRepository(Country, ARepository):
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
        request = "INSERT INTO Countries(CountryName, CountryCode, NatLangCode, CurrencyCode) VALUES (\""+obj.CountryName+"\", \""+obj.CountryCode+"\", \""+str(obj.NatLangCode)+"\", \""+obj.CurrencyCode+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM Countries WHERE CountryId = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE Countries SET CountryName = '" + obj.CountryName + "',CountryCode = '" + obj.CountryCode + "', NatLangCode = " + str(obj.NatLangCode) + ", CurrencyCode = '" + obj.CurrencyCode + "' WHERE CountryId= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[Country]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT CountryId, CountryName, CountryCode, NatLangCode, CurrencyCode FROM Countries"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            country = Country()
            country.load(each)
            ls.append(country)
        return ls

    def get_id(self, id) -> Country:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM Countries WHERE CountryId = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        country = Country()
        country.load(fetch)
        return country

    