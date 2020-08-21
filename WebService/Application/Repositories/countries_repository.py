from Application.Models.country import Country
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists
import os


class CountriesRepository:
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

    @staticmethod
    def add(country):
        connection = sqlite3.connect(CountriesRepository.sqlite_path)
        c = connection.cursor()
        c.execute("INSERT INTO Countries (CountryName, CountryCode, NatLangCode, CurrencyCode) VALUES (\""+country.CountryName+"\",\""+country.CountryCode+"\","+str(country.NatLangCode)+",\""+country.CurrencyCode+"\");")
        connection.commit()
        c.close()
        connection.close()

    @staticmethod
    def delete(id):
        connection = sqlite3.connect(CountriesRepository.sqlite_path)
        c = connection.cursor()
        c.execute("DELETE FROM Countries WHERE CountryId = "+str(id)+";")
        connection.commit()
        c.close()
        connection.close()

    @staticmethod
    def edit(id, obj):
        sql = "UPDATE Countries SET CountryName = '" + obj.CountryName + "', CountryCode = '" + obj.CountryCode + "', NatLangCode = " + str(obj.NatLangCode) + ", CurrencyCode = '" + obj.CurrencyCode + "' WHERE CountryId = " + str(id) + ";"
        connection = sqlite3.connect(CountriesRepository.sqlite_path)
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
        c.close()
        connection.close()

    @staticmethod
    def get():
        connection = sqlite3.connect(CountriesRepository.sqlite_path)
        c = connection.cursor()
        ls = c.execute("SELECT CountryId, CountryName, CountryCode, NatLangCode, CurrencyCode FROM Countries")
        return str(c.fetchall())

    @staticmethod
    def get_id(id):
        connection = sqlite3.connect(CountriesRepository.sqlite_path)
        c = connection.cursor()
        ls = c.execute("SELECT * FROM Countries WHERE CountryId = " + str(id))
        return str(c.fetchone())
