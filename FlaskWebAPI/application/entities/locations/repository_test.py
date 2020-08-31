from application.entities.locations.repository import LocationsRepository
from application.entities.locations.model_test import temp_location


a = LocationsRepository()

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
    a.post(1, temp_location())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_location())

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

