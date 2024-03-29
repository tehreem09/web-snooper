import json


def search_records():
    cleaned_data = open('lifetech_cleandata.json')
    data = json.load(cleaned_data)
    my_dic={}

    for record in data:
        number = record.get("number")
        cnic = record.get("cnic")

        my_dic=record
        my_dic= basic_info_merger(my_dic)


        result01 = search_taxpayers_record(cnic)
        result02 = search_redbook_record(cnic, number)
        result03 = search_terrorists_record(cnic, number)
        print(f'[+] searching for number > {number}')

        result = {}

        if result01 is not None:
            result =  merge_found_records(my_dic, result01)
            if result02 and result03 is not None:
                result = merge_found_records(my_dic, result01, result02, result03)
            elif result02 is not None:
                result = merge_found_records(my_dic, result01, result02)
            elif result03 is not None:
                result = merge_found_records(my_dic, result01, result03)

        if result02 is not None:
            result = result02
            if result03 is not None:
                result = merge_found_records(my_dic ,result02, result03)
                print(result)

        elif result03 is not None:
            result = merge_found_records(my_dic, result03)

        else:
            result = (my_dic)


        main_dbt_handler(number, result)

# def basic_info_merger(dict):
#     with open ('basic_number_info.json', 'r') as basic_num_info:
#         num_info = json.load(basic_num_info)
#     for data in num_info:
#         # print(data)
#         number = str(data.get('number'))[2:-2]
#         # print(number)
#         number2 = '+92'+ dict['number']
#         # print ("with" + number2)
#         if ('+92'+dict['number'])==number:
#             print("number matcheddd")
#             new_dict = merge_found_records(dict, data)
#             return new_dict
#     return dict

def basic_info_merger(dict):
    with open ('basic_number_info.json', 'r') as basic_num_info:
        num_info = json.load(basic_num_info)
    for data in num_info:
        # print(data)
        number = data.get('number')
        # print(number)
        number2 = '+92'+ dict['number']
        # print ("with" + number2)
        if ('+92'+dict['number'])==number:
            print("number matcheddd")
            new_dict = merge_found_records(dict, data)
            return new_dict
    return dict

def merge_found_records(*dicts):
    return {
      k: [d[k] for d in dicts if k in d]
      for k in set(k for d in dicts for k in d)
    }


def search_taxpayers_record(cnic):
    with open('snooper/sheet7.json', 'r') as tax_payers:
        tax_payers = json.load(tax_payers)

    for records in tax_payers['Sheet1']:
        tax_payers_dictionary = {}
        if cnic == records['NTN']:
#             tax_payers_dictionary['CNIC'] = cnic
            tax_payers_dictionary['BUSINESS_NAME'] = records['BUSINESS_NAME']
            tax_payers_dictionary['NAME REGISTERED TO'] = records['NAME']

            return tax_payers_dictionary


def search_redbook_record(cnic, number):
    with open('snooper/redbook.json', 'r') as redbook:
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
    with open('snooper/data.json', 'r') as terrorists:
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


# import json


# def search_records():
#     cleaned_data = open('lifetech_cleandata.json')
#     data = json.load(cleaned_data)
#     my_dic={}

#     for record in data:
#         number = record.get("number")
#         cnic = record.get("cnic")

#         my_dic=record
#         lifetech_dic = {}
#         lifetech_dic['NAME'] = record['name']
#         lifetech_dic['CNIC'] = record['cnic']
#         lifetech_dic['PHONE NUM'] = record['number']
#         if 'city' in my_dic:
#             lifetech_dic['CITY'] = record['city']
#         if 'address'in my_dic:
#             lifetech_dic['ADDRESS'] = record['address']

#         result01 = search_taxpayers_record(cnic)
#         result02 = search_redbook_record(cnic, number)
#         result03 = search_terrorists_record(cnic, number)
#         print(f'[+] searching for number > {number}')

#         result = {}

#         if result01 is not None:
#             result =  merge_found_records(lifetech_dic, result01)
#             if result02 and result03 is not None:
#                 result = merge_found_records(lifetech_dic, result01, result02, result03)
#             elif result02 is not None:
#                 result = merge_found_records(lifetech_dic, result01, result02)
#             elif result03 is not None:
#                 result = merge_found_records(lifetech_dic, result01, result03)

#         elif result02 is not None:
#             result = result02
#             if result03 is not None:
#                 result = merge_found_records(lifetech_dic ,result02, result03)
#                 print(result)

#         elif result03 is not None:
#             result = merge_found_records(lifetech_dic, result03)

#         else:
#             result= lifetech_dic

#         main_dbt_handler(number, result)


# def merge_found_records(*dicts):
#     return {
#       k: [d[k] for d in dicts if k in d]
#       for k in set(k for d in dicts for k in d)
#     }


# def search_taxpayers_record(cnic):
#     with open('snooper/sheet7.json', 'r') as tax_payers:
#         tax_payers = json.load(tax_payers)

#     for records in tax_payers['Sheet1']:
#         tax_payers_dictionary = {}
#         if cnic == records['NTN']:
# #             tax_payers_dictionary['CNIC'] = cnic
#             tax_payers_dictionary['BUSINESS_NAME'] = records['BUSINESS_NAME']
#             tax_payers_dictionary['NAME REGISTERED TO'] = records['NAME']

#             return tax_payers_dictionary


# def search_redbook_record(cnic, number):
#     with open('snooper/redbook.json', 'r') as redbook:
#         redbook = json.load(redbook)

#     for data2 in redbook:
#         redbook_dictionary = {}
#         if cnic == (data2['CNIC']):
# #             redbook_dictionary['CNIC'] = cnic
#             redbook_dictionary['F/NAME'] = data2['PARENTAGE']
#             redbook_dictionary['ADDRESS'] = data2['ADDRESS']
#             redbook_dictionary['PHONE NUM'] = data2['PHONE NUM']
#             redbook_dictionary['FIR'] = data2['FIR no.']

#             return redbook_dictionary


# def search_terrorists_record(cnic, number):
#     with open('snooper/data.json', 'r') as terrorists:
#         terrorists = json.load(terrorists)

#     for data2 in terrorists:
#         terrorists_dictionary = {}
#         if cnic == (data2['CNIC']):
# #             terrorists_dictionary['CNIC'] = cnic
#             terrorists_dictionary['F/NAME'] = data2['FNAME']
#             terrorists_dictionary['ADDRESS'] = data2['ADDRESS']
#             terrorists_dictionary['REWARD'] = data2['REWARD']
#             terrorists_dictionary['FIR'] = data2['FIR']
#             terrorists_dictionary['RELIGIOUS/POLITICAL AFFILIATION'] = data2['RELIGIOUS/POLITICAL AFFILIATION']

#             return terrorists_dictionary


# def main_dbt_handler(number, record):
#     if record:
#         with open('main_dbt.json', 'a+') as main_dbt:
#             json.dump(record, main_dbt, indent=4)
#             main_dbt.write('\n')
#             main_dbt.close()
#             print(str(record)+'\n')
#     else:
#         print('[-] No criminal record found....\n[-] No business or tax payers record fount....\n')


# search_records()




# import json


# def search_records():
#     cleaned_data = open('lifetech_cleandata.json')
#     data = json.load(cleaned_data)

#     for record in data:
#         number = record.get("number")
#         cnic = record.get("cnic")

#         result01 = search_taxpayers_record(cnic)
#         result02 = search_redbook_record(cnic, number)
#         result03 = search_terrorists_record(cnic, number)
#         print(f'[+] searching for number > {number}')

#         result = {}

#         if result01 is not None:
#             result = result01
#             if result02 and result03 is not None:
#                 result = merge_found_records(result01, result02, result03)
#             elif result02 is not None:
#                 result = merge_found_records(result01, result02)
#             elif result03 is not None:
#                 result = merge_found_records(result01, result03)

#         elif result02 is not None:
#             result = result02
#             if result03 is not None:
#                 result = merge_found_records(result02, result03)

#         elif result03 is not None:
#             result = merge_found_records(result03)

#         main_dbt_handler(number, result)


# def merge_found_records(*dicts):
#     return {
#       k: [d[k] for d in dicts if k in d]
#       for k in set(k for d in dicts for k in d)
#     }


# def search_taxpayers_record(cnic):
#     with open('sheet7.json', 'r') as tax_payers:
#         tax_payers = json.load(tax_payers)

#     for records in tax_payers['Sheet1']:
#         tax_payers_dictionary = {}
#         if cnic == records['NTN']:
# #             tax_payers_dictionary['CNIC'] = cnic
#             tax_payers_dictionary['BUSINESS_NAME'] = records['BUSINESS_NAME']
#             tax_payers_dictionary['NAME REGISTERED TO'] = records['NAME']

#             return tax_payers_dictionary


# def search_redbook_record(cnic, number):
#     with open('redbook.json', 'r') as redbook:
#         redbook = json.load(redbook)

#     for data2 in redbook:
#         redbook_dictionary = {}
#         if cnic == (data2['CNIC']):             
# #             redbook_dictionary['CNIC'] = cnic
#             redbook_dictionary['F/NAME'] = data2['PARENTAGE']
#             redbook_dictionary['ADDRESS'] = data2['ADDRESS']
#             redbook_dictionary['PHONE NUM'] = data2['PHONE NUM']
#             redbook_dictionary['FIR'] = data2['FIR no.']

#             return redbook_dictionary


# def search_terrorists_record(cnic, number):
#     with open('data.json', 'r') as terrorists:
#         terrorists = json.load(terrorists)

#     for data2 in terrorists:
#         terrorists_dictionary = {}
#         if cnic == (data2['CNIC']):            
# #             terrorists_dictionary['CNIC'] = cnic
#             terrorists_dictionary['F/NAME'] = data2['FNAME']
#             terrorists_dictionary['ADDRESS'] = data2['ADDRESS']
#             terrorists_dictionary['REWARD'] = data2['REWARD']
#             terrorists_dictionary['FIR'] = data2['FIR']

#             return terrorists_dictionary


# def main_dbt_handler(number, record):
#     if record:
#         with open('main_dbt.json', 'a+') as main_dbt:
#             json.dump(record, main_dbt, indent=4)
#             main_dbt.write('\n')
#             main_dbt.close()
#             print(str(record)+'\n')
#     else:
#         print('[-] No criminal record found....\n[-] No business or tax payers record fount....\n')


# search_records()
