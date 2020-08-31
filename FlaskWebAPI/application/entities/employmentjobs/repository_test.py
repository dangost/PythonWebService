from application.entities.employmentjobs.repository import EmploymentJobsRepository
from application.entities.employmentjobs.model_test import temp_employmentjobs


a = EmploymentJobsRepository()

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
    a.post(1, temp_employmentjobs())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_employmentjobs())

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

