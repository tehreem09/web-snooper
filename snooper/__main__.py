#!/usr/bin/python

import json
import argparse
from scrapy.crawler import CrawlerProcess
from . import numberhandler
from . import lifetechcrawlerpy
from . import ec2tos3


def arg_parser():
    parser = argparse.ArgumentParser(usage="snooper [options] +0xxxxxxxxxx", description=('DESCRIPTION \n'
                                                                                          'Snooper is a command line '
                                                                                          'OSINT based tool used for '
                                                                                          'finding phone number and/or '
                                                                                          'email address owner\'s PII '
                                                                                          'information. '))
    parser.add_argument("-e", "--email", dest="email", type=str, help='email on which you want to perform snooping')
    parser.add_argument("-n", "--name", dest="name", type=str, help='name on which you want to perform snooping')
    parser.add_argument("-c", "--company", dest="my_company", type=str,
                        help='company on which you want to perform snooping')
    parser.add_argument("-o", "--occupation", dest="occ", type=str,
                        help='occupation on which you want to perform snooping')
    parser.add_argument("-s", "--surname", dest="surname", type=str,
                        help='surname on which you want to perform snooping')
    arg_logic(parser.parse_args())


def arg_logic(args_values):
    if args_values.email:
        print(args_values.email)
        if args_values.name:
            print(args_values.name)
            if args_values.surname:
                print(args_values.surname)
                if args_values.occ:
                    print(args_values.occ)
                    if args_values.my_company:
                        print(args_values.my_company)

                elif args_values.my_company:
                    print(args_values.my_company)
            elif args_values.occ:
                print(args_values.occ)
                if args_values.my_company:
                    print(args_values.my_company)
                    if args_values.surname:
                        print(args_values.surname)

            elif args_values.my_company:
                print(args_values.my_company)
                if args_values.surname:
                    print(args_values.surname)
                    if args_values.occ:
                        print(args_values.occ)

        elif args_values.surname:
            print(args_values.surname)
            if args_values.name:
                print(args_values.name)
                if args_values.occ:
                    print(args_values.occ)
                    if args_values.my_company:
                        print(args_values.my_company)

                elif args_values.my_company:
                    print(args_values.my_company)
                    if args_values.occ:
                        print(args_values.occ)

            elif args_values.occ:
                print(args_values.occ)
                if args_values.my_company:
                    print(args_values.my_company)
                    if args_values.name:
                        print(args_values.name)

            elif args_values.my_company:
                print(args_values.my_company)

        elif args_values.occ:
            print(args_values.occ)
            if args_values.name:
                print(args_values.name)
                if args_values.my_company:
                    print(args_values.my_company)
                    if args_values.surname:
                        print(args_values.surname)

                elif args_values.surname:
                    print(args_values.surname)
                    if args_values.my_company:
                        print(args_values.my_company)

            elif args_values.surname:
                print(args_values.surname)
                if args_values.my_company:
                    print(args_values.my_company)
                    if args_values.name:
                        print(args_values.name)
                elif args_values.name:
                    print(args_values.name)
                    if args_values.my_company:
                        print(args_values.my_company)
            elif args_values.my_company:
                print(args_values.my_company)
                if args_values.surname:
                    print(args_values.surname)
                    if args_values.name:
                        print(args_values.name)
                elif args_values.name:
                    print(args_values.name)
                    if args_values.surname:
                        print(args_values.surname)

        elif args_values.my_company:
            print(args_values.my_company)
            if args_values.name:
                print(args_values.name)
                if args_values.occ:
                    print(args_values.occ)
                    if args_values.surname:
                        print(args_values.surname)

                elif args_values.surname:
                    print(args_values.surname)
                    if args_values.occ:
                        print(args_values.occ)

            elif args_values.surname:
                print(args_values.surname)
                if args_values.occ:
                    print(args_values.occ)
                    if args_values.name:
                        print(args_values.name)
                elif args_values.name:
                    print(args_values.name)
                    if args_values.occ:
                        print(args_values.occ)
            elif args_values.occ:
                print(args_values.occ)
                if args_values.surname:
                    print(args_values.surname)
                    if args_values.name:
                        print(args_values.name)
                elif args_values.name:
                    print(args_values.name)
                    if args_values.surname:
                        print(args_values.surname)

    else:
        print(' [-] please enter email')


def db_check():
    pass


def number_basic_info(numbers, countries):

    obj = numberhandler.NumberRecon(numbers=numbers, countries=countries)
    number_basic_data_dict = obj.get_number_origin_data()
    with open('basic_number_info.json', 'w') as fp:
        json.dump(number_basic_data_dict, fp, indent=4)
    fp.close()
    ec2tos3.upload_file_to_s3bucket('', 'basic_number_info.json', 'number_basic_info.json')


def live_search():
    process = CrawlerProcess(settings={"FEEDS": {"raw_data.json": {"format": "json"}},
                                       'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
                                       'LOG_FILE': 'logs',
                                       'LOG_LEVEL': 'CRITICAL'
                                       })
    process.crawl(lifetechcrawlerpy.LifetechCrawler)
    process.start()
    ec2tos3.upload_file_to_s3bucket('', 'lifetech_rawdata.json', 'lifetechdata.json')
    pass


def file_handler():



def main():
    arg_parser()
    if db_check():
        pass
    else:
        numbers = ['+923362314059', '+923362314059', '+61449765241', '+12017237150']
        countries = ['PK', None, None, None]
        number_basic_info(numbers, countries)
        # live_search()
        numbers = ['+923362314059', '+923362314059', '+61449765241', '+12017237150']
        x = len(numbers)
        countries = [None] * x
        obj = numberhandler.NumberRecon(numbers=numbers, countries=countries)
        number_basic_data_dict = obj.get_number_origin_data()
        with open('basic_number_info.json', 'w') as fp:
            json.dump(number_basic_data_dict, fp, indent=4)
        fp.close()

    file = open('demo_numbers.txt', 'r')
    numbers_list = [line.strip('\n')+',' for line in file.readlines()]
    print(numbers_list)


if __name__ == '__main__':
    main()
    print("..................end.................")
