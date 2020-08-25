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

from Application.Abstraction.abs_repository import ARepository


def countries_controller_init():
    return ARepository(CountriesRepository)


def customers_controller_init():
    return ARepository(CustomersRepository)


def customercompanies_controller_init():
    return ARepository(CustomerCompaniesRepository)


def customeremployees_controller_init():
    return ARepository(CustomerEmployeesRepository)


def employments_controller_init():
    return ARepository(EmploymentsRepository)


def employmentjobs_controller_init():
    return ARepository(EmploymentJobsRepository)


def inventories_controller_init():
    return ARepository(InventoriesRepository)


def locations_controller_init():
    return ARepository(LocationsRepository)


def orderitems_controller_init():
    return ARepository(OrderItemsRepository)


def orders_controller_init():
    return ARepository(OrdersRepository)


def people_controller_init():
    return ARepository(PeopleRepository)


def personlocations_controller_init():
    return ARepository(PersonLocationsRepository)


def phonenumbers_controller_init():
    return ARepository(PhoneNumbersRepository)


def products_controller_init():
    return ARepository(ProductsRepository)


def restrictedinfo_controller_init():
    return ARepository(RestrictedInfoRepository)


def warehouses_controller_init():
    return ARepository(WarehousesRepository)

