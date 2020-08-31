from application.entities.restrictedinfo.repository import RestrictedInfoRepository
from application.entities.restrictedinfo.model_test import temp_restrictedinfo


a = RestrictedInfoRepository()

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
    a.post(1, temp_restrictedinfo())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_restrictedinfo())

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

