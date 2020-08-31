from application.entities.people.repository import PeopleRepository
from application.entities.people.model_test import temp_person


a = PeopleRepository()

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
    a.post(1, temp_person())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_person())

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

