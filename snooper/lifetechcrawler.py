import requests
import json
from bs4 import BeautifulSoup

from . import lifetech_cleaner

num_data={}
mainlist=[]

def crawl(numbers):
  for n in numbers:
    indlist=[]

    try:
      url = 'http://lifetech.tech/?number={}'.format(n)
      page = requests.get(url)
      soup = BeautifulSoup(page.content, 'html.parser')

      for td in soup.findAll("td"):
        if td.find('b') is None:
          data=(td.text.strip())
          indlist.append(data)
      num_data['number_data']=indlist
      copy= num_data.copy()
      mainlist.append(copy)


    except Exception as err:
      print(err)
      continue

  print(mainlist)

  with open('lifetech_rawdata.json', 'w') as outfile:
    json.dump(mainlist, outfile)
    lifetech_cleaner.clean()


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

