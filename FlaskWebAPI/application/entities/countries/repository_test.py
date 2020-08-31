from application.entities.countries.repository import CountriesRepository
from application.entities.countries.model_test import temp_country


a = CountriesRepository()

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
    a.post(1, temp_country())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_country())

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

