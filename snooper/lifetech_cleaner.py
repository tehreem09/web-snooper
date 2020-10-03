import json
import re

newfile=open('E:/adeena/semester 7/fyp/cleandatalt.json', 'w')

mainlist=[]
cities=['KARACHI', 'Karachi', 'LAHORE', 'Faisalabad','SIALKOT,Punjab','Gujranwala', 'Gilgit', 'KARACHI,Sindh', 'CHITRAL',
        'CHICHA_WATNI,Punjab', 'GWADER,Baluchistan', 'MARDAN,Khyber Pakhtunkhwa', 'CHAKWAL', 'LHR', 'ISLAMABAD,Punjab',
        'PAKPATTAN,Punjab']



with open('C:/Users/zunai/Downloads/lifetechdata (1).json') as lifetech_raw_file:
    data = json.load(lifetech_raw_file)
    for dictionary in data:
        mainlist.append(dictionary.get('number_data'))
    listt=[]
    for eachlist in mainlist:
        data = {}
        nameflag = False
        address = False
        for value in eachlist:
            if re.match("^[0-9]{13}", value):
                data['cnic'] = value
            if re.match("^\d{10}$", value):
                data['number'] = value
            for city in cities:
                if value == city:
                    data['city'] = value
            if not nameflag:
                if re.match("[a-z]|[A-Z]", value):
                    name = value
                    nameflag = True
                    data['name'] = value
            elif nameflag:
                if not address:
                    if re.match("[A-Z-][A-Za-z-/0-9#.,:]*[ ]+", value):
                        data['address'] = value
                        address = True
        listt.append(data)


json.dump(listt, newfile)


