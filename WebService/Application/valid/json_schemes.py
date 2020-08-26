class Schemes:
    country_json = {"CountryName": {"type": "string", "minlength": 1},
                    "CountryCode": {"type": "string", "minlength": 1},
                    "NatLangCode": {"type": "integer"},
                    "CurrencyCode": {"type": "string", "minlength": 1}}

    customer_json = {"CustomerId": {"type": "integer"},
                     "PersonId": {"type": "integer"},
                     "CustomerEmployeeId": {"type": "integer"},
                     "AccountMgrId": {"type": "integer"},
                     "IncomeLevel": {"type": "integer"}}

    customercompany_json = {"CompanyName": {"type": "string", "minlength": 1},
                            "CompanyCreditLimit": {"type": "integer"},
                            "CreditLimitCurrency": {"type": "string", "minlength": 1}}

    customeremployee_json = {"CompanyId": {"type": "integer"},
                             "BadgeNumber": {"type": "string", "minlength": 1},
                             "JobTitle": {"type": "string", "minlength": 1},
                             "Department": {"type": "string", "minlength": 1},
                             "CreditLimit": {"type": "integer"},
                             "CreditLimitCurrency": {"type": "string", "minlength": 1}}

    employmentjobs_json = {"CountriesCountryId": {"type": "integer"},
                       "JobTitle": {"type": "string", "minlength": 1},
                       "MinSalary": {"type": "integer"},
                       "MaxSalary": {"type": "integer"}}

    employment_json = {"PersonId": {"type": "integer"},
                       "HRJobId":  {"type": "integer"},
                       "ManagerEmployeeId": {"type": "integer"},
                       "StartDate":  {"type": "string", "minlength": 1},
                       "EndDate": {"type": "string", "minlength": 1},
                       "Salary":  {"type": "integer"},
                       "CommissionPercent":  {"type": "integer"},
                       "Employmentcol":  {"type": "string", "minlength": 1}}

    inventory_json = {"ProductId":  {"type": "integer"},
                      "WarehouseId":  {"type": "integer"},
                      "QuantityOnHand":  {"type": "integer"},
                      "QuantityAvailable":  {"type": "integer"}}

    location_json = {"CountryId": {"type": "integer"},
                     "AdressLine1": {"type": "string", "minlength": 1},
                     "AdressLine2":  {"type": "string", "minlength": 1},
                     "City":  {"type": "string", "minlength": 1},
                     "State":  {"type": "string", "minlength": 1},
                     "District":  {"type": "string", "minlength": 1},
                     "PostalCode":  {"type": "string", "minlength": 1},
                     "LocationTypeCode":  {"type": "integer"},
                     "Description": {"type": "string", "minlength": 1},
                     "ShippingNotes":  {"type": "string", "minlength": 1},
                     "CountriesCountryId": {"type": "integer"}}

    orderitem_json = {"OrderId":  {"type": "integer"},
                      "ProductId":  {"type": "integer"},
                      "UnitPrice":  {"type": "integer"},
                      "Quantity":  {"type": "integer"}}

    orders_json = {"SalesRepId": {"type": "integer"},
                   "OrderDate":  {"type": "string", "minlength": 1},
                   "OrderCode":  {"type": "integer"},
                   "OrderStatus":  {"type": "string", "minlength": 1},
                   "OrderTotal":  {"type": "integer"},
                   "OrderCurrency":  {"type": "string", "minlength": 1},
                   "PromotionCode":  {"type": "string", "minlength": 1}}

    person_json = {"FirstName":  {"type": "string", "minlength": 1},
                   "LastName":  {"type": "string", "minlength": 1},
                   "MiddleName":  {"type": "string", "minlength": 1},
                   "Nickname":  {"type": "string", "minlength": 1},
                   "NatLangCode":  {"type": "integer"},
                   "CultureCode":  {"type": "integer"},
                   "Gender":  {"type": "string", "minlength": 1}}

    personlocation_json = {"PersonsPersonId":  {"type": "integer"},
                           "LocationsLocationsId":  {"type": "integer"},
                           "SubAdress": {"type": "string", "minlength": 1},
                           "LocationUsage":  {"type": "string", "minlength": 1},
                           "Notes":  {"type": "string", "minlength": 1}}

    phonenumber_json = {"PeoplePersonId":  {"type": "integer"},
                        "LocationLocationId":  {"type": "integer"},
                        "Phonenumber": {"type": "integer"},
                        "CountryCode":  {"type": "integer"},
                        "PhoneType":  {"type": "integer"}}

    product_json = {"ProductName":  {"type": "string", "minlength": 1},
                    "Description":  {"type": "string", "minlength": 1},
                    "Category":  {"type": "integer"},
                    "WeightClass":  {"type": "integer"},
                    "WarrantlyPeriod":  {"type": "integer"},
                    "SupplierId":  {"type": "integer"},
                    "Status":  {"type": "string", "minlength": 1},
                    "ListPrice":  {"type": "integer"},
                    "MinimumPrice":  {"type": "integer"},
                    "PriceCurrency":  {"type": "string", "minlength": 1},
                    "CatalogURL":  {"type": "string", "minlength": 1}}

    restrictedinfo_json = {"PersonId":  {"type": "integer"},
                           "DateOfBirth":  {"type": "string", "minlength": 1},
                           "DateOfDeath":  {"type": "string", "minlength": 1},
                           "GovernmentId":  {"type": "string", "minlength": 1},
                           "PassportId":  {"type": "string", "minlength": 1},
                           "HireDire":  {"type": "string", "minlength": 1},
                           "SeniorityCode":  {"type": "integer"}}

    warehouse_json = {"WarehouseId":  {"type": "integer"},
                      "LocationId":  {"type": "integer"},
                      "WarehouseName":  {"type": "string", "minlength": 1}}

