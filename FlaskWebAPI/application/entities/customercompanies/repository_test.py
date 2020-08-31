from application.entities.customercompanies.repository import CustomerCompaniesRepository
from application.entities.customercompanies.model_test import temp_customercompany


a = CustomerCompaniesRepository()

# get
t = True
try:
    a.get()

except BaseException:
    t = False
assert t


# post
t = True
try:
    a.post(1, temp_customercompany())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_customercompany())

except BaseException:
    t = False
assert t

# delete
t = True
try:
    a.delete(1)

except BaseException:
    t = False
assert t

