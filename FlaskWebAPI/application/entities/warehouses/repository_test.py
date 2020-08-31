from application.entities.warehouses.repository import WarehousesRepository
from application.entities.warehouses.model_test import temp_warehouse


a = WarehousesRepository()

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
    a.post(1, temp_warehouse())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_warehouse())

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

