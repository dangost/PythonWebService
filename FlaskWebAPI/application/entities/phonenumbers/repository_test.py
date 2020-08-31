from application.entities.phonenumbers.repository import PhoneNumbersRepository
from application.entities.phonenumbers.model_test import temp_phonenumber


a = PhoneNumbersRepository()

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
    a.post(1, temp_phonenumber())

except BaseException:
    t = False
assert t

# put
t = True
try:
    a.put(1, temp_phonenumber())

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

