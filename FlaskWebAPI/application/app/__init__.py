from application.entities.countries.interface import BaseCountriesRepository
from application.entities.customers.interface import BaseCustomersRepository
from application.entities.customercompanies.interface import BaseCustomerCompaniesRepository
from application.entities.customeremployees.interface import BaseCustomerEmployeesRepository
from application.entities.employments.interface import BaseEmploymentsRepository
from application.entities.employmentjobs.interface import BaseEmploymentJobsRepository
from application.entities.inventories.interface import BaseInventoriesRepository
from application.entities.locations.interface import BaseLocationsRepository
from application.entities.orderitems.interface import BaseOrderItemsRepository
from application.entities.orders.interface import BaseOrdersRepository
from application.entities.people.interface import BasePeopleRepository
from application.entities.personlocations.interface import BasePersonLocationsRepository
from application.entities.phonenumbers.interface import BasePhoneNumbersRepository
from application.entities.products.interface import BaseProductsRepository
from application.entities.restrictedinfo.interface import BaseRestrictedInfoRepository
from application.entities.warehouse.interface import BaseWarehousesRepository

from application.entities.countries.repository import CountriesRepository
from application.entities.customers.repository import CustomersRepository
from application.entities.customercompanies.repository import CustomerCompaniesRepository
from application.entities.customeremployees.repository import CustomerEmployeesRepository
from application.entities.employments.repository import EmploymentsRepository
from application.entities.employmentjobs.repository import EmploymentJobsRepository
from application.entities.inventories.repository import InventoriesRepository
from application.entities.locations.repository import LocationsRepository
from application.entities.orderitems.repository import OrderItemsRepository
from application.entities.orders.repository import OrdersRepository
from application.entities.people.repository import PeopleRepository
from application.entities.personlocations.repository import PersonLocationsRepository
from application.entities.phonenumbers.repository import PhoneNumbersRepository
from application.entities.products.repository import ProductsRepository
from application.entities.restrictedinfo.repository import RestrictedInfoRepository
from application.entities.warehouse.repository import WarehousesRepository


from application.db import sqlite
sqlite.load()


countries_db: BaseCountriesRepository = CountriesRepository()

customers_db: BaseCustomersRepository = CustomersRepository()

customercompanies_db: BaseCustomerCompaniesRepository = CustomerCompaniesRepository()

customeremployees_db: CustomerEmployeesRepository = CustomerEmployeesRepository()

employments_db: BaseEmploymentsRepository = EmploymentsRepository()

employmentjobs_db: BaseEmploymentJobsRepository = EmploymentJobsRepository()

inventories_db: BaseInventoriesRepository = InventoriesRepository()

locations_db: BaseLocationsRepository = LocationsRepository()

orderitems_db: BaseOrderItemsRepository = OrderItemsRepository()

orders_db: BaseOrdersRepository = OrdersRepository()

people_db: BasePeopleRepository = PeopleRepository()

personlocations_db: BasePersonLocationsRepository = PersonLocationsRepository()

phonenumbers_db: BasePhoneNumbersRepository = PhoneNumbersRepository()

products_db: BaseProductsRepository = ProductsRepository()

restrictedinfo_db: BaseRestrictedInfoRepository = RestrictedInfoRepository()

warehouses_db: BaseWarehousesRepository = WarehousesRepository()


