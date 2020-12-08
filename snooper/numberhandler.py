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

    def multiple_number_handler(self):
        for number, country in list(zip(self.numbers, self.countries)):
            if self.number_validity_check(number, country):
                self.parsed_numbers.append(self.parsed_number)
                self.data_dict['number']=(number)
            else:
                print('[-] Following number is not valid and/or possible >', number)

    def number_validity_check(self, number, country):
        try:
            self.parsed_number = phonenumbers.parse(number, country)
            phonenumbers.is_valid_number(self.parsed_number)
            phonenumbers.is_possible_number(self.parsed_number)
            return True
        except phonenumbers.NumberParseException:
            print('[-] Please provide the following phone number in International format or provide Region', number)
            return False

    def number_country_name(self, parsed_number):
        return geocoder.description_for_number(parsed_number, 'en')

    def number_timezone(self, parsed_number):
        print(timezone.time_zones_for_number(parsed_number))
        new= str(timezone.time_zones_for_number(parsed_number))[2:-3]
        print (new)
        return new

    def number_carrier(self, parsed_number):
        print(parsed_number)
        return carrier.name_for_number(parsed_number, 'en')

    def get_number_origin_data(self):
        main_list = []
        self.multiple_number_handler()

        for p_number in self.parsed_numbers:
            print(p_number)
            self.data_dict['country']=(self.number_country_name(p_number))
            self.data_dict['time_zone']=(self.number_timezone(p_number))
            self.data_dict['carrier']=(self.number_carrier(p_number))

        main_list.append(self.data_dict)

        return main_list


# class NumberRecon:
#     def __init__(self, **kwargs):
#         self.numbers = kwargs['numbers']
#         self.countries = kwargs['countries']
#         self.parsed_numbers = []
#         self.parsed_number = None
#         self.data_dict = defaultdict(list)

#     def multiple_number_handler(self):
#         for number, country in list(zip(self.numbers, self.countries)):
#             if self.number_validity_check(number, country):
#                 self.parsed_numbers.append(self.parsed_number)
#                 self.data_dict['number'].append(number)
#             else:
#                 print('[-] Following number is not valid and/or possible >', number)

#     def number_validity_check(self, number, country):
#         try:
#             self.parsed_number = phonenumbers.parse(number, country)
#             phonenumbers.is_valid_number(self.parsed_number)
#             phonenumbers.is_possible_number(self.parsed_number)
#             return True
#         except phonenumbers.NumberParseException:
#             print('[-] Please provide the following phone number in International format or provide Region', number)
#             return False

#     def number_country_name(self, parsed_number):
#         return geocoder.description_for_number(parsed_number, 'en')

#     def number_timezone(self, parsed_number):
#         return timezone.time_zones_for_number(parsed_number)

#     def number_carrier(self, parsed_number):
#         return carrier.name_for_number(parsed_number, 'en')

#     def get_number_origin_data(self):
#         self.multiple_number_handler()
#         for p_number in self.parsed_numbers:
#             self.data_dict['country'].append(self.number_country_name(p_number))
#             self.data_dict['time_zone'].append(self.number_timezone(p_number))
#             self.data_dict['carrier'].append(self.number_carrier(p_number))
#         return self.data_dict
