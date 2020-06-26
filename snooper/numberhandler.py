#!/usr/bin/env python3

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from _collections import defaultdict


class NumberRecon:
    def __init__(self, **kwargs):
        self.numbers = kwargs['numbers']
        self.countries = kwargs['countries']
        self.parsed_numbers = []
        self.parsed_number = None
        self.data_dict = defaultdict(list)
        self.x = 0

    def multiple_number_handler(self):
        for number, country in list(zip(self.numbers, self.countries)):
            self.x = self.x + 1
            if self.number_validity_check(number, country):
                self.parsed_numbers.append(self.parsed_number)
                # parsed_number = phonenumbers.parse(number, country)
                # number_origin_info = self.get_number_origin_data(number, parsed_number)
            else:
                print('[-] Following number is not valid and/or possible >', number)

    def number_validity_check(self, number, country):
        try:
            print(self.x)
            print(number, country)
            self.parsed_number = phonenumbers.parse(number, country)
            print(self.parsed_number)
            phonenumbers.is_valid_number(self.parsed_number)
            phonenumbers.is_possible_number(self.parsed_number)
            return True
        except phonenumbers.NumberParseException:
            print('[-] Please provide the following phone number in International format or provide Region', number)
            return False

    def number_country_name(self, parsed_number):
        return geocoder.description_for_number(parsed_number, 'en')

    def number_timezone(self, parsed_number):
        return timezone.time_zones_for_number(parsed_number)

    def number_carrier(self, parsed_number):
        return carrier.name_for_number(parsed_number, 'en')

    def get_number_origin_data(self):
        self.multiple_number_handler()
        for p_number in self.parsed_numbers:
            self.data_dict['number'].append(p_number)
            self.data_dict['country'].append(self.number_country_name(p_number))
            self.data_dict['time_zone'].append(self.number_timezone(p_number))
            self.data_dict['carrier'].append(self.number_carrier(p_number))
        # if self.data_dict:
        #     print('blah')
        #     return False
        return self.data_dict


numbers = ['+923362314059', '+923362314059', '+923362314059', '03362314059', '03362314059', '03362314059', '+923362314',
           '+923362314', '+923362314', '03362314', '03362314', '03362314']
countries = ['PK', None, 'GB', 'PK', None, 'GB', 'PK', None, 'GB', 'PK', None, 'GB']

# numbers = ['+923362314059', '03362314059', '+923362314', '03362314']
# countries = [None, 'PK', 'PK', 'PK']

obj = NumberRecon(numbers=numbers, countries=countries)
obj.get_number_origin_data()
for key, value in obj.data_dict.items():
    print(key, value)

# check_country = phonenumbers.parse('+923362314059', 'CH')
# print(check_country, 'Country: ', geocoder.description_for_number(check_country, 'en'))
# gb_number = phonenumbers.parse("+447986123456", None)
# print(timezone.time_zones_for_number(gb_number))
# ro_number = phonenumbers.parse("+40721234567", "RO")
# print(ro_number, 'Carrier: ', carrier.name_for_number(ro_number, "en"))
