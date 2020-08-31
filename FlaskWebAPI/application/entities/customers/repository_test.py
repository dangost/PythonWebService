from application.entities.customers.repository import CustomersRepository
from application.entities.customers.model_test import temp_customer


a = CustomersRepository()

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
    a.post(1, temp_customer())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_customer())

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

