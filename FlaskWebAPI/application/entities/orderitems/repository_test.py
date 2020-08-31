from application.entities.orderitems.repository import OrderItemsRepository
from application.entities.orderitems.model_test import temp_orderitem


a = OrderItemsRepository()

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
    a.post(1, temp_orderitem())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_orderitem())

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

