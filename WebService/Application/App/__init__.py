from Application.Abstraction.abs_repository import ARepository
from Application.Repositories.countries_repository import CountriesRepository
from Application.Repositories.customers_repository import CustomersRepository
from Application.Repositories.customercompanies_repository import CustomerCompaniesRepository
from Application.Repositories.customeremployees_repository import CustomerEmployeesRepository
from Application.Repositories.employments_repository import EmploymentsRepository
from Application.Repositories.employmentjobs_repository import EmploymentJobsRepository
from Application.Repositories.inventories_repository import InventoriesRepository
from Application.Repositories.locations_repository import LocationsRepository
from Application.Repositories.orderitems_repository import OrderItemsRepository
from Application.Repositories.orders_repository import OrdersRepository
from Application.Repositories.people_repository import PeopleRepository
from Application.Repositories.personlocations_repository import PersonLocationsRepository
from Application.Repositories.phonenumbers_repository import PhoneNumbersRepository
from Application.Repositories.products_repository import ProductsRepository
from Application.Repositories.restrictedinfo_repository import RestrictedInfoRepository
from Application.Repositories.warehouses_repository import WarehousesRepository

countries_db: ARepository = CountriesRepository()

customers_db: ARepository = CustomersRepository()

customercompanies_db: ARepository = CustomerCompaniesRepository()

customeremployees_db: ARepository = CustomerEmployeesRepository()

employments_db: ARepository = EmploymentsRepository()

employmentjobs_db: ARepository = EmploymentJobsRepository()

inventories_db: ARepository = InventoriesRepository()

locations_db: ARepository = LocationsRepository()

orderitems_db: ARepository = OrderItemsRepository()

orders_db: ARepository = OrdersRepository()

people_db: ARepository = PeopleRepository()

personlocations_db: ARepository = PersonLocationsRepository()

phonenumbers_db: ARepository = PhoneNumbersRepository()

products_db: ARepository = ProductsRepository()

restrictedinfo_db: ARepository = RestrictedInfoRepository()

warehouses_db: ARepository = WarehousesRepository()

