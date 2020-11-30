import json


def search_records():
    cleaned_data = open('lifetech_cleandata.json')
    data = json.load(cleaned_data)
    my_dic={}

    for record in data:
        number = record.get("number")
        cnic = record.get("cnic")

        my_dic=record
        lifetech_dic = {}
        lifetech_dic['NAME'] = record['name']
        lifetech_dic['CNIC'] = record['cnic']
        lifetech_dic['PHONE NUM'] = record['number']
        if 'city' in my_dic:
            lifetech_dic['CITY'] = record['city']
        if 'address'in my_dic:
            lifetech_dic['ADDRESS'] = record['address']

        result01 = search_taxpayers_record(cnic)
        result02 = search_redbook_record(cnic, number)
        result03 = search_terrorists_record(cnic, number)
        print(f'[+] searching for number > {number}')

        result = {}

        if result01 is not None:
            result =  merge_found_records(lifetech_dic, result01)
            if result02 and result03 is not None:
                result = merge_found_records(lifetech_dic, result01, result02, result03)
            elif result02 is not None:
                result = merge_found_records(lifetech_dic, result01, result02)
            elif result03 is not None:
                result = merge_found_records(lifetech_dic, result01, result03)

        elif result02 is not None:
            result = result02
            if result03 is not None:
                result = merge_found_records(lifetech_dic ,result02, result03)
                print(result)

        elif result03 is not None:
            result = merge_found_records(lifetech_dic, result03)

        else:
            result= lifetech_dic

        main_dbt_handler(number, result)


def merge_found_records(*dicts):
    return {
      k: [d[k] for d in dicts if k in d]
      for k in set(k for d in dicts for k in d)
    }


def search_taxpayers_record(cnic):
    with open('sheet7.json', 'r') as tax_payers:
        tax_payers = json.load(tax_payers)

    for records in tax_payers['Sheet1']:
        tax_payers_dictionary = {}
        if cnic == records['NTN']:
#             tax_payers_dictionary['CNIC'] = cnic
            tax_payers_dictionary['BUSINESS_NAME'] = records['BUSINESS_NAME']
            tax_payers_dictionary['NAME REGISTERED TO'] = records['NAME']

            return tax_payers_dictionary


def search_redbook_record(cnic, number):
    with open('redbook.json', 'r') as redbook:
        redbook = json.load(redbook)

    for data2 in redbook:
        redbook_dictionary = {}
        if cnic == (data2['CNIC']):
#             redbook_dictionary['CNIC'] = cnic
            redbook_dictionary['F/NAME'] = data2['PARENTAGE']
            redbook_dictionary['ADDRESS'] = data2['ADDRESS']
            redbook_dictionary['PHONE NUM'] = data2['PHONE NUM']
            redbook_dictionary['FIR'] = data2['FIR no.']

            return redbook_dictionary


def search_terrorists_record(cnic, number):
    with open('data.json', 'r') as terrorists:
        terrorists = json.load(terrorists)

    for data2 in terrorists:
        terrorists_dictionary = {}
        if cnic == (data2['CNIC']):
#             terrorists_dictionary['CNIC'] = cnic
            terrorists_dictionary['F/NAME'] = data2['FNAME']
            terrorists_dictionary['ADDRESS'] = data2['ADDRESS']
            terrorists_dictionary['REWARD'] = data2['REWARD']
            terrorists_dictionary['FIR'] = data2['FIR']
            terrorists_dictionary['RELIGIOUS/POLITICAL AFFILIATION'] = data2['RELIGIOUS/POLITICAL AFFILIATION']

            return terrorists_dictionary


def main_dbt_handler(number, record):
    if record:
        with open('main_dbt.json', 'a+') as main_dbt:
            json.dump(record, main_dbt, indent=4)
            main_dbt.write('\n')
            main_dbt.close()
            print(str(record)+'\n')
    else:
        print('[-] No criminal record found....\n[-] No business or tax payers record fount....\n')


search_records()




# #!/usr/bin/env python3

# import phonenumbers
# from phonenumbers import geocoder
# from phonenumbers import carrier
# from phonenumbers import timezone
# from _collections import defaultdict


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
