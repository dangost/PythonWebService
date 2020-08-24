from Application.Models.restrictedinfo import RestrictedInfo
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists


class RestrictedInfoRepository:
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
        request = "INSERT INTO RestrictedInfo(DateOfBirth, DateOfDeath, GovernmentId, PassportId, HireDire, SeniorityCode) VALUES (\""+obj.DateOfBirth+"\", \""+obj.DateOfDeath+"\", \""+obj.GovernmentId+"\", \""+obj.PassportId+"\", \""+obj.HireDire+"\", \""+str(obj.SeniorityCode)+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM RestrictedInfo WHERE  = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj):
        request = "UPDATE RestrictedInfo SET DateOfBirth = '" + obj.DateOfBirth + "',DateOfDeath = '" + obj.DateOfDeath + "',GovernmentId = '" + obj.GovernmentId + "',PassportId = '" + obj.PassportId + "',HireDire = '" + obj.HireDire + "',SeniorityCode = '" + str(obj.SeniorityCode) + " WHERE = "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT , DateOfBirth, DateOfDeath, GovernmentId, PassportId, HireDire, SeniorityCode FROM RestrictedInfo"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            restrictedinfo = RestrictedInfo()
            restrictedinfo.load(each)
            ls.append(restrictedinfo.to_json())
        return str(ls)

    def get_id(self, id):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM RestrictedInfo WHERE  = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        restrictedinfo = RestrictedInfo()
        restrictedinfo.load(fetch)
        return str(restrictedinfo.to_json())

    