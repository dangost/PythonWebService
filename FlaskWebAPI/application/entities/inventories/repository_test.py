from application.entities.inventories.repository import InventoriesRepository
from application.entities.inventories.model_test import temp_inventory


a = InventoriesRepository()

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
    a.post(1, temp_inventory())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_inventory())

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

