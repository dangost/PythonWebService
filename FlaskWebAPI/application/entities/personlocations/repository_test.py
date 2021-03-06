from application.entities.personlocations.repository import PersonLocationsRepository
from application.entities.personlocations.model_test import temp_personlocation


a = PersonLocationsRepository()

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
    a.post(1, temp_personlocation())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_personlocation())

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

