from Application.Models.personlocation import PersonLocation
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists


class PersonLocationsRepository:
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
        request = "INSERT INTO PersonLocations(LocationsLocationsId, SubAdress, LocationUsage, Notes) VALUES (\""+str(obj.LocationsLocationsId)+"\", \""+obj.SubAdress+"\", \""+obj.LocationUsage+"\", \""+obj.Notes+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM PersonLocations WHERE  = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj):
        request = "UPDATE PersonLocations SET LocationsLocationsId = '" + str(obj.LocationsLocationsId) + "',SubAdress = '" + obj.SubAdress + "',LocationUsage = '" + obj.LocationUsage + "',Notes = '" + obj.Notes + " WHERE = "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT , LocationsLocationsId, SubAdress, LocationUsage, Notes FROM PersonLocations"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            personlocation = PersonLocation()
            personlocation.load(each)
            ls.append(personlocation.to_json())
        return str(ls)

    def get_id(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM PersonLocations WHERE  = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        personlocation = PersonLocation()
        personlocation.load(fetch)
        return str(personlocation.to_json())

    