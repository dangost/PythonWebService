from Application.Models.employmentjobs import EmploymentJobs
import Application.BaseSupport.SQLiteSupport as Base
import sqlite3
from os import _exists as file_exists
from typing import List
from Application.Abstraction.abs_repository import ARepository


class EmploymentJobsRepository(EmploymentJobs, ARepository):
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
        request = "INSERT INTO EmploymentJobs(CountriesCountryId, JobTitle, MinSalary, MaxSalary) VALUES (\""+str(obj.CountriesCountryId)+"\", \""+obj.JobTitle+"\", \""+str(obj.MinSalary)+"\", \""+str(obj.MaxSalary)+"\");"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def delete(self, id) -> None:
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        request = "DELETE FROM EmploymentJobs WHERE HRJobId = "+str(id)+";"
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def edit(self, id, obj) -> None:
        request = "UPDATE EmploymentJobs SET CountriesCountryId = " + str(obj.CountriesCountryId) + ",JobTitle = '" + obj.JobTitle + "',MinSalary = " + str(obj.MinSalary) + ",MaxSalary = " + str(obj.MaxSalary) + " WHERE HRJobId= "+str(id)+";"
        connection = sqlite3.connect(self.sqlite_path)
        c = connection.cursor()
        c.execute(request)
        connection.commit()
        c.close()
        connection.close()

    def get(self) -> List[EmploymentJobs]:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT HRJobId, CountriesCountryId, JobTitle, MinSalary, MaxSalary FROM EmploymentJobs"
        cursor.execute(request)
        fetch = cursor.fetchall()
        ls = []
        for each in fetch:
            employmentjobs = EmploymentJobs()
            employmentjobs.load(each)
            ls.append(employmentjobs)
        return ls

    def get_id(self, id) -> EmploymentJobs:
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()
        request = "SELECT * FROM EmploymentJobs WHERE HRJobId = "+str(id)
        cursor.execute(request)
        fetch = cursor.fetchone()
        employmentjobs = EmploymentJobs()
        employmentjobs.load(fetch)
        return employmentjobs

    