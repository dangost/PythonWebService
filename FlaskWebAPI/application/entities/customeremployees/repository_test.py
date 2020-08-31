from application.entities.customeremployees.repository import CustomerEmployeesRepository
from application.entities.customeremployees.model_test import temp_customeremployee


a = CustomerEmployeesRepository()

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
    a.post(1, temp_customeremployee())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_customeremployee())

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

