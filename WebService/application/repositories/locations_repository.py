from application.models.location import Location
import application.base_support.sqlite_support as base
import sqlite3
from os import _exists as file_exists
from typing import List
from application.abstraction.base_repository import BaseRepository


class LocationsRepository(Location, BaseRepository):
    sqlite_path = "sqlite.db"

    def add(self, obj) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "INSERT INTO Locations(CountryId, AdressLine1, AdressLine2, City, State, District, PostalCode, LocationTypeCode, Description, ShippingNotes, CountriesCountryId) VALUES (\""+str(obj.CountryId)+"\", \""+obj.AdressLine1+"\", \""+obj.AdressLine2+"\", \""+obj.City+"\", \""+obj.State+"\", \""+obj.District+"\", \""+obj.PostalCode+"\", \""+str(obj.LocationTypeCode)+"\", \""+obj.Description+"\", \""+obj.ShippingNotes+"\", \""+str(obj.CountriesCountryId)+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM Locations WHERE LocationId = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE Locations SET CountryId = " + str(obj.CountryId) + ",AdressLine1 = '" + obj.AdressLine1 + "',AdressLine2 = '" + obj.AdressLine2 + "',City = '" + obj.City + "',State = '" + obj.State + "',District = '" + obj.District + "',PostalCode = '" + obj.PostalCode + "',LocationTypeCode = " + str(obj.LocationTypeCode) + ",Description = '" + obj.Description + "',ShippingNotes = '" + obj.ShippingNotes + "',CountriesCountryId = " + str(obj.CountriesCountryId) + " WHERE LocationId= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[Location]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT LocationId, CountryId, AdressLine1, AdressLine2, City, State, District, PostalCode, LocationTypeCode, Description, ShippingNotes, CountriesCountryId FROM Locations"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            location = Location()
            location.load(each)
            ls.append(location)
        return ls

    def get_id(self, id) -> Location:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM Locations WHERE LocationId = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        location = Location()
        location.load(fetch)
        return location

    