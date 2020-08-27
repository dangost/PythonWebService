from Application.Models.employment import Employment
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists
from typing import List
from Application.Abstraction.abs_repository import ARepository


class EmploymentsRepository(Employment, ARepository):
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
        request = "INSERT INTO Employments(PersonId, HRJobId, ManagerEmployeeId, StartDate, EndDate, Salary, CommissionPercent, Employmentcol) VALUES (\""+str(obj.PersonId)+"\", \""+str(obj.HRJobId)+"\", \""+str(obj.ManagerEmployeeId)+"\", \""+obj.StartDate+"\", \""+obj.EndDate+"\", \""+str(obj.Salary)+"\", \""+str(obj.CommissionPercent)+"\", \""+obj.Employmentcol+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM Employments WHERE EmployeeID = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE Employments SET PersonId = " + str(obj.PersonId) + ",HRJobId = " + str(obj.HRJobId) + ",ManagerEmployeeId = " + str(obj.ManagerEmployeeId) + ",StartDate = '" + obj.StartDate + "',EndDate = '" + obj.EndDate + "',Salary = " + str(obj.Salary) + ",CommissionPercent = " + str(obj.CommissionPercent) + ",Employmentcol = '" + obj.Employmentcol + "' WHERE EmployeeID= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[Employment]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT EmployeeID, PersonId, HRJobId, ManagerEmployeeId, StartDate, EndDate, Salary, CommissionPercent, Employmentcol FROM Employments"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            employment = Employment()
            employment.load(each)
            ls.append(employment)
        return ls

    def get_id(self, id) -> Employment:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM Employments WHERE EmployeeID = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        employment = Employment()
        employment.load(fetch)
        return employment

    