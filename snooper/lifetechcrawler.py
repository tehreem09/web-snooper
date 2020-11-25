import requests
import json
from bs4 import BeautifulSoup



numbers = ['3422817264', '3424224229']

success = 0
fail = 0
#crawler
for n in numbers:

  try:
    url = 'http://lifetech.tech/?number={}'.format(n)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for td in soup.findAll("td"):
      # print (td)
      if td.find('b') is None:
        data=(td.text.strip())
        print (data)
        with open('lifetech_rawdata.json', 'a') as outfile:
            json.dump(data, outfile)

  except Exception as err:
    print(err)
    fail += 1
    continue



# import scrapy


# class Lifetech_Crawler(scrapy.Spider):
#     name = "Lifetech"
#     custom_settings = {
#             'FEED_URI': 'lifetech_rawdata.json',
#             'FEED_FORMAT': 'json',
#             'FEED_EXPORTERS': {
#                 'json': 'scrapy.exporters.JsonItemExporter',
#             },
#             'FEED_EXPORT_ENCODING': 'utf-8',
#         }

#     def __init__(self, numbers=[]):
#         self.numbers = numbers
#         super().__init__()

#     def start_requests(self):
#         print("strt request")
#         for j in self.numbers:
#             try:
#                 urls = 'http://lifetech.tech/?number={}'.format(j)
#                 print("going to parse")
#                 yield scrapy.Request(url=urls, callback=self.parse())
#             except Exception as err:
#                 print(err)
#                 continue

#     def parse(self, response):
#         print("parse started")
#         for tr in response.css('table'):
#             print("Problem strts here....")
# #             title = tr.xpath('//tr//td//strong/text()').extract()
#             title = tr.xpath('//td//strong/text()').extract()
#             print(title)
#             if not title:
#                 print("failed")
#             else:
#                 # self.success += 1
#                 yield {'number_data': title}


# # import scrapy
# #
# #
# # class LifetechCrawler(scrapy.Spider):
# #     name = "Lifetech"
# #     numbers = ['3216386601', '3408372640']
# #     custom_settings = {
# #         'FEED_URI': 'lifetech_rawdata.json',
# #         'FEED_FORMAT': 'json',
# #         'FEED_EXPORTERS': {
# #             'json': 'scrapy.exporters.JsonItemExporter',
# #         },
# #         'FEED_EXPORT_ENCODING': 'utf-8',
# #     }
# #
# #     def start_requests(self):
# #         for i in self.numbers:
# #             urls = 'http://lifetech.tech/?number={}'.format(i)
# #             yield scrapy.Request(url=urls, callback=self.parse)
# #
# #     def parse(self, response):
# #         for tr in response.css('table'):
# #             title = tr.xpath('//tr//td//strong/text()').extract()
# #             yield {'titlestext': title}
