#!/usr/bin/python

# import argparse
# from . import __init__
from scrapy.crawler import CrawlerProcess
from . import testscraper

def main():
    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.
    # parser = argparse.ArgumentParser(usage="snooper [options] +0xxxxxxxxxx", description=('DESCRIPTION \n'
    #                                                                                       'Snooper is a command line '
    #                                                                                       'osint based tool used for '
    #                                                                                       'finding phone number and/or '
    #                                                                                       'email address owner\'s PII '
    #                                                                                       'information. '))

    # parser.add_argument("-n", "--number", dest="number", required=int, help='phone number on which you want to
    # perform ' 'snooping')
    # parser.add_argument("")
    # args_values = parser.parse_args()
    print("finally")
    pass


if __name__ == '__main__':
    main()
    import sys

    for x in sys.path:
        print(x)

    print("..............................................................................................")
    process = CrawlerProcess(settings={"FEEDS": {"item01.json": {"format": "json"}},
                                       'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})
    process.crawl(testscraper.QuotesScraper)

    print("........ before process.start() ........")
    process.start()
    print("end")
# if __name__ == '__main__':
#     class MySpider(scrapy.Spider):
#         # Your spider definition
#         ...
#
#
#     process = CrawlerProcess({
#         'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#     })
#
#     process.crawl(BlogSpider)
#     process.start()
