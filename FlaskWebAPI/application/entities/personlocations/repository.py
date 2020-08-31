from application.entities.personlocations.model import PersonLocation
import application.entities.personlocations.schema as base
import sqlite3
from typing import List
from application.entities.personlocations.interface import BasePersonLocationsRepository


class PersonLocationsRepository(BasePersonLocationsRepository):
    sqlite_path = "sqlite.db"

    def add(self, obj) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "INSERT INTO PersonLocations(LocationsLocationId, SubAdress, LocationUsage, Notes) VALUES (\"" + str(
            obj.LocationsLocationsId) + "\", \"" + obj.SubAdress + "\", \"" + obj.LocationUsage + "\", \"" + obj.Notes + "\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM PersonLocations WHERE PersonsPersonId = " + str(id) + ";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE PersonLocations SET SubAdress = '" + obj.SubAdress + "',LocationUsage = '" + obj.LocationUsage + "',Notes = '" + obj.Notes + "' WHERE LocationsLocationId = " + str(
            id) + ";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[PersonLocation]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT PersonsPersonId, LocationsLocationId, SubAdress, LocationUsage, Notes FROM PersonLocations"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            personlocation = PersonLocation()
            personlocation.load(each)
            ls.append(personlocation)
        return ls

    def get_id(self, id) -> PersonLocation:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT PersonsPersonId, LocationsLocationId, SubAdress, LocationUsage, Notes FROM PersonLocations WHERE LocationsLocationId = " + str(
            id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        personlocation = PersonLocation()
        personlocation.load(fetch)
        return personlocation


    