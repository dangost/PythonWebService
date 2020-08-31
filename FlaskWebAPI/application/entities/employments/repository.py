from application.entities.employments.model import Employment
import application.entities.employments.schema as base
import sqlite3
from typing import List
from application.entities.employments.interface import BaseEmploymentsRepository


class EmploymentsRepository(BaseEmploymentsRepository):
    sqlite_path = "sqlite.db"

    def add(self, obj) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "INSERT INTO Employments(PersonId, HRJobId, ManagerEmployeeId, StartDate, EndDate, Salary, CommissionPercent, Employmentcol) VALUES (\"" + str(
            obj.PersonId) + "\", \"" + str(obj.HRJobId) + "\", \"" + str(
            obj.ManagerEmployeeId) + "\", \"" + obj.StartDate + "\", \"" + obj.EndDate + "\", \"" + str(
            obj.Salary) + "\", \"" + str(obj.CommissionPercent) + "\", \"" + obj.Employmentcol + "\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM Employments WHERE EmployeeID = " + str(id) + ";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE Employments SET PersonId = " + str(obj.PersonId) + ",HRJobId = " + str(
            obj.HRJobId) + ",ManagerEmployeeId = " + str(
            obj.ManagerEmployeeId) + ",StartDate = '" + obj.StartDate + "',EndDate = '" + obj.EndDate + "',Salary = " + str(
            obj.Salary) + ",CommissionPercent = " + str(
            obj.CommissionPercent) + ",Employmentcol = '" + obj.Employmentcol + "' WHERE EmployeeID= " + str(id) + ";"
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
        request = "SELECT * FROM Employments WHERE EmployeeID = " + str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        employment = Employment()
        employment.load(fetch)
        return employment

    