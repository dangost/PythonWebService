from application.entities.restrictedinfo.model import RestrictedInfo
import application.entities.restrictedinfo.schema as base
import sqlite3
from typing import List
from application.entities.restrictedinfo.interface import BaseRestrictedInfoRepository


class RestrictedInfoRepository(BaseRestrictedInfoRepository):
    sqlite_path = "sqlite.db"

    def add(self, obj) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "INSERT INTO RestrictedInfoes (PersonId, DateOfBirth, DateOfDeath, GovernmentId, PassportId, HireDire, SeniorityCode) VALUES (" + str(
            obj.PersonId) + ", \"" + obj.DateOfBirth + "\", \"" + obj.DateOfDeath + "\", \"" + obj.GovernmentId + "\", \"" + obj.PassportId + "\", \"" + obj.HireDire + "\", " + str(
            obj.SeniorityCode) + ");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM RestrictedInfoes WHERE PersonId  = " + str(id) + ";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE RestrictedInfoes SET PersonId = " + str(
            obj.PersonId) + ", DateOfBirth = '" + obj.DateOfBirth + "',DateOfDeath = '" + obj.DateOfDeath + "',GovernmentId = '" + obj.GovernmentId + "',PassportId = '" + obj.PassportId + "',HireDire = '" + obj.HireDire + "', SeniorityCode = " + str(
            obj.SeniorityCode) + " WHERE PersonId = " + str(id) + ";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[RestrictedInfo]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT PersonId, DateOfBirth, DateOfDeath, GovernmentId, PassportId, HireDire, SeniorityCode FROM RestrictedInfoes"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            restrictedinfo = RestrictedInfo()
            restrictedinfo.load(each)
            ls.append(restrictedinfo)
        return ls

    def get_id(self, id) -> RestrictedInfo:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM RestrictedInfoes WHERE PersonId = " + str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        restrictedinfo = RestrictedInfo()
        restrictedinfo.load(fetch)
        return restrictedinfo
    