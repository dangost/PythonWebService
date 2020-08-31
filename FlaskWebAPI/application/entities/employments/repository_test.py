from application.entities.employments.repository import EmploymentsRepository
from application.entities.employments.model_test import temp_employment


a = EmploymentsRepository()

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
    a.post(1, temp_employment())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_employment())

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

