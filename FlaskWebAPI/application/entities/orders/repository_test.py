from application.entities.orders.repository import OrdersRepository
from application.entities.orders.model_test import temp_orders


a = OrdersRepository()

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
    a.post(1, temp_orders())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_orders())

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

