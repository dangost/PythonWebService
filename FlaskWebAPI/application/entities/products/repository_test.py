from application.entities.products.repository import ProductsRepository
from application.entities.products.model_test import temp_product


a = ProductsRepository()

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
    a.post(1, temp_product())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_product())

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

