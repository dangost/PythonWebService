from Application.Models.country import Country
import sqlite3


class CountriesRepository:
    sqlite_path = "sqlite.db"

    def load(self):
        file = open(self.sqlite_path, 'w')
        pass

    def add(self, country):
        pass

    def delete(self, id):
        pass

    def get(self):
        pass

    def get_id(self, id):
        pass
