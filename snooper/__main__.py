#!/usr/bin/python

import json
import argparse
from scrapy.crawler import CrawlerProcess
from . import numberhandler
from . import lifetechcrawler
from . import lifetech_cleaner
from . import db_hadler
from . import ec2tos3


def arg_parser():
    parser = argparse.ArgumentParser(usage="snooper [options] +0xxxxxxxxxx", description=('DESCRIPTION \n'
                                                                                          'Snooper is a command line '
                                                                                          'OSINT based tool used for '
                                                                                          'finding phone number and/or '
                                                                                          'email address owner\'s PII '
                                                                                          'information. '))
    # parser.add_argument("-e", "--email", dest="email", type=str, help='email on which you want to perform snooping')
    parser.add_argument("-n", "--number", dest="number", type=int, help='name on which you want to perform snooping')
    parser.add_argument('-f', '--file', dest='filename', type=argparse.FileType('r'), help='name or path to file of '
                                                                                           'simple text file having '
                                                                                           'number in each line.')
    return parser.parse_args()


def db_check(numbers):
    pass


def number_basic_info(numbers):
    x = len(numbers)
    countries = [None] * x
    obj = numberhandler.NumberRecon(numbers=numbers, countries=countries)
    number_basic_data_dict = obj.get_number_origin_data()
    with open('basic_number_info.json', 'a') as fp:
        json.dump(number_basic_data_dict, fp, indent=4)
    fp.close()
    ec2tos3.upload_file_to_s3bucket('', 'basic_number_info.json', 'number_basic_info.json')


def live_search(numbers):
    process = CrawlerProcess(settings={"FEEDS": {"raw_data.json": {"format": "json"}},
                                       'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
                                       'LOG_FILE': 'logs',
                                       'LOG_LEVEL': 'CRITICAL'
                                       })
#     process.crawl(lifetechcrawler.Lifetech_Crawler, numbers)
#     process.start()
    lifetechcrawler.crawl(numbers)
    print("copy ec2-s3")
    ec2tos3.upload_file_to_s3bucket('', 'lifetech_rawdata.json', 'lifetechdata.json')
    lifetech_cleaner.clean()


def file_handler(filename):
    file = open(filename.name, 'r')
    numberswithcode = [line.strip('\n') for line in file.readlines()]
    file = open(filename.name, 'r')
    numberswithoutcode = [line.strip('\n')[3:] for line in file.readlines()]
    file.close()
    return numberswithcode, numberswithoutcode


def main():
    arg_values = arg_parser()
    if arg_values.number:
        numberswithcode = ['+'+str(arg_values.number)]
        numberswithoutcode = [str(arg_values.number)[2:]]
        print(numberswithcode, numberswithoutcode)
        if db_check(numberswithcode):
            pass
        else:
            number_basic_info(numberswithcode)
            live_search(numberswithoutcode)
#             db_hadler.search_records()
    elif arg_values.filename:
        numberswithcode, numberswithoutcode = file_handler(arg_values.filename)
        if db_check(numberswithcode):
            pass
        else:
            number_basic_info(numberswithcode)
            live_search(numberswithoutcode)
#             db_hadler.search_records()


if __name__ == '__main__':
    main()
    print("..................end.................")
