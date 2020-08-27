from application.models.phonenumber import PhoneNumber
import application.base_support.sqlite_support as base
import sqlite3
from os import _exists as file_exists
from typing import List
from application.abstraction.base_repository import BaseRepository


class PhoneNumbersRepository(PhoneNumber, BaseRepository):
    sqlite_path = "sqlite.db"

    def add(self, obj) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "INSERT INTO PhoneNumbers(PeoplePersonId, LocationsLocationId, Phonenumber, CountryCode, PhoneType) VALUES (\""+str(obj.PeoplePersonId)+"\", \""+str(obj.LocationLocationId)+"\", \""+str(obj.Phonenumber)+"\", \""+str(obj.CountryCode)+"\", \""+str(obj.PhoneType)+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM PhoneNumbers WHERE PhoneNumberId = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE PhoneNumbers SET PeoplePersonId = " + str(obj.PeoplePersonId) + ",LocationsLocationId = " + str(obj.LocationLocationId) + ",Phonenumber = " + str(obj.Phonenumber) + ",CountryCode = " + str(obj.CountryCode) + ",PhoneType = " + str(obj.PhoneType) + " WHERE PhoneNumberId= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[PhoneNumber]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT PhoneNumberId, PeoplePersonId, LocationsLocationId, Phonenumber, CountryCode, PhoneType FROM PhoneNumbers"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            phonenumber = PhoneNumber()
            phonenumber.load(each)
            ls.append(phonenumber)
        return ls

    def get_id(self, id) -> PhoneNumber:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM PhoneNumbers WHERE PhoneNumberId = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        phonenumber = PhoneNumber()
        phonenumber.load(fetch)
        return phonenumber

    