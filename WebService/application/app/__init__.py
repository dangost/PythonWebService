from application.abstraction.base_repository import BaseRepository
from application.repositories.countries_repository import CountriesRepository
from application.repositories.customers_repository import CustomersRepository
from application.repositories.customercompanies_repository import CustomerCompaniesRepository
from application.repositories.customeremployees_repository import CustomerEmployeesRepository
from application.repositories.employments_repository import EmploymentsRepository
from application.repositories.employmentjobs_repository import EmploymentJobsRepository
from application.repositories.inventories_repository import InventoriesRepository
from application.repositories.locations_repository import LocationsRepository
from application.repositories.orderitems_repository import OrderItemsRepository
from application.repositories.orders_repository import OrdersRepository
from application.repositories.people_repository import PeopleRepository
from application.repositories.personlocations_repository import PersonLocationsRepository
from application.repositories.phonenumbers_repository import PhoneNumbersRepository
from application.repositories.products_repository import ProductsRepository
from application.repositories.restrictedinfo_repository import RestrictedInfoRepository
from application.repositories.warehouses_repository import WarehousesRepository

from application.base_support import sqlite_support
sqlite_support.load()


countries_db: BaseRepository = CountriesRepository()

customers_db: BaseRepository = CustomersRepository()

customercompanies_db: BaseRepository = CustomerCompaniesRepository()

customeremployees_db: BaseRepository = CustomerEmployeesRepository()

employments_db: BaseRepository = EmploymentsRepository()

employmentjobs_db: BaseRepository = EmploymentJobsRepository()

inventories_db: BaseRepository = InventoriesRepository()

locations_db: BaseRepository = LocationsRepository()

orderitems_db: BaseRepository = OrderItemsRepository()

orders_db: BaseRepository = OrdersRepository()

people_db: BaseRepository = PeopleRepository()

personlocations_db: BaseRepository = PersonLocationsRepository()

phonenumbers_db: BaseRepository = PhoneNumbersRepository()

products_db: BaseRepository = ProductsRepository()

restrictedinfo_db: BaseRepository = RestrictedInfoRepository()

warehouses_db: BaseRepository = WarehousesRepository()


