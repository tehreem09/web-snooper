#!/usr/bin/env python3

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


x = phonenumbers.parse("+442083661177", None)
a = phonenumbers.parse("+92343286650", None)
y = phonenumbers.parse("020 8366 1177", "GB")
z = phonenumbers.parse("00 1 650 253 2222", "GB")  # as dialled from GB, not a GB number
print(x, '\n', a, '\n', y, '\n', z)
print('type:', type(x))
print('....................................................')
b = phonenumbers.parse("+120012301", None)
check_false = 'possible' if phonenumbers.is_possible_number(b) else 'not possible'  # too few digits for USA
validity_false = 'valid' if phonenumbers.is_valid_number(b) else 'not valid'
print(b, check_false)
print(b, validity_false)
check_true = 'possible' if phonenumbers.is_possible_number(z) else 'not possible'  # too few digits for USA
validity_true = 'valid' if phonenumbers.is_valid_number(z) else 'not valid'
print(z, check_true)
print(z, validity_true)
print('....................................................')
try:
    c = phonenumbers.parse("02081234567", None)
    d = phonenumbers.parse("gibberish", None)
except phonenumbers.NumberParseException:
    print("plz write correct phone number")
else:
    print('out of try except')
print('....................................................')
check_country = phonenumbers.parse('+923362314059', 'CH')
print(check_country, 'Country: ', geocoder.description_for_number(check_country, 'en'))
print('....................................................')
ro_number = phonenumbers.parse("+40721234567", "RO")
print(ro_number, 'Carrier: ', carrier.name_for_number(ro_number, "en"))
print(check_country, 'Carrier: ', carrier.name_for_number(check_country, 'en'))
print('.......................................................')
gb_number = phonenumbers.parse("+447986123456", None)
print(timezone.time_zones_for_number(gb_number))
print(timezone.time_zones_for_number(check_country))