from application.models.person import Person
import application.base_support.sqlite_support as base
import sqlite3
from os import _exists as file_exists
from typing import List
from application.abstraction.base_repository import BaseRepository


class PeopleRepository(Person, BaseRepository):
    sqlite_path = "sqlite.db"

    def add(self, obj) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "INSERT INTO People(FirstName, LastName, MiddleName, Nickname, NatLangCode, CultureCode, Gender) VALUES (\""+obj.FirstName+"\", \""+obj.LastName+"\", \""+obj.MiddleName+"\", \""+obj.Nickname+"\", \""+str(obj.NatLangCode)+"\", \""+str(obj.CultureCode)+"\", \""+obj.Gender+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM People WHERE Id = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE People SET FirstName = '" + obj.FirstName + "',LastName = '" + obj.LastName + "',MiddleName = '" + obj.MiddleName + "',Nickname = '" + obj.Nickname + "',NatLangCode = " + str(obj.NatLangCode) + ",CultureCode = " + str(obj.CultureCode) + ",Gender = '" + obj.Gender + "' WHERE Id= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[Person]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT Id, FirstName, LastName, MiddleName, Nickname, NatLangCode, CultureCode, Gender FROM People"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            person = Person()
            person.load(each)
            ls.append(person)
        return ls

    def get_id(self, id) -> Person:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM People WHERE Id = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        person = Person()
        person.load(fetch)
        return person

    