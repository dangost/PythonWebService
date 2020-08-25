from Application.Abstraction.abs_repository import ARepository

from Application.Repositories.countries_repository import CountriesRepository
countries_db: ARepository = CountriesRepository()

from Application.Repositories.customers_repository import CustomersRepository
customers_db: ARepository = CustomersRepository()

from Application.Repositories.customercompanies_repository import CustomerCompaniesRepository
customercompanies_db: ARepository = CustomerCompaniesRepository()

from Application.Repositories.customeremployees_repository import CustomerEmployeesRepository
customeremployees_db: ARepository = CustomerEmployeesRepository()

from Application.Repositories.employments_repository import EmploymentsRepository
employments_db: ARepository = EmploymentsRepository()

from Application.Repositories.employmentjobs_repository import EmploymentJobsRepository
employmentjobs_db: ARepository = EmploymentJobsRepository()

from Application.Repositories.inventories_repository import InventoriesRepository
inventories_db: ARepository = InventoriesRepository()

from Application.Repositories.locations_repository import LocationsRepository
locations_db: ARepository = LocationsRepository()
from Application.Repositories.orderitems_repository import OrderItemsRepository
orderitems_db: ARepository = OrderItemsRepository()

from Application.Repositories.orders_repository import OrdersRepository
orders_db: ARepository = OrdersRepository()

from Application.Repositories.people_repository import PeopleRepository
people_db: ARepository = PeopleRepository()

from Application.Repositories.personlocations_repository import PersonLocationsRepository
personlocations_db: ARepository = PersonLocationsRepository()

from Application.Repositories.phonenumbers_repository import PhoneNumbersRepository
phonenumbers_db: ARepository = PhoneNumbersRepository()

from Application.Repositories.products_repository import ProductsRepository
products_db: ARepository = ProductsRepository()

from Application.Repositories.restrictedinfo_repository import RestrictedInfoRepository
restrictedinfo_db: ARepository = RestrictedInfoRepository()

from Application.Repositories.warehouses_repository import WarehousesRepository
warehouses_db: ARepository = WarehousesRepository()

