#!/usr/bin/python

from scrapy.crawler import CrawlerProcess
from . import testscraper
import argparse


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

    # elif args_values.name:
    #         print(args_values.name)
    #         if args_values.email:
    #             print(args_values.email)
    #             if args_values.surname:
    #                 print(args_values.surname)
    #                 if args_values.occ:
    #                     print(args_values.occ)
    #                     if args_values.my_company:
    #                         print(args_values.my_company)

    else:
        print(' [-] please enter email')
    # elif args_values.my_company:
    #     print(args_values.my_company)


def main():
    arg_parser()


if __name__ == '__main__':
    main()
    print("..............................................................................................")
    process = CrawlerProcess(settings={"FEEDS": {"item01.json": {"format": "json"}},
                                       'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
                                       'LOG_FILE': 'logs',
                                       'LOG_LEVEL': 'CRITICAL'
                                       })
    process.crawl(testscraper.QuotesScraper)

    print("........ before process.start() ........")
    process.start()
    print("................end.............")
