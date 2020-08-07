import scrapy
import requests
from scrapy.crawler import CrawlerProcess


class Lifetech_Crawler(scrapy.Spider):
  name = "Lifetech"
  numbers = ['3216386601','3408372640']

  def start_requests(self):
    for i in self.numbers:
        urls = 'http://lifetech.tech/?number={}'.format(i)
        yield scrapy.Request(url=urls, callback=self.parse)

  def parse(self, response):
    for tr in response.css('table'):
      title=tr.xpath('//tr//td//strong/text()').extract()
      #  title=response.css('table').extract()
      yield{'titlestext':title}

    

process = CrawlerProcess(settings={"FEEDS": {"item01.json": {"format": "json"}},'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)', 'LOG_FILE': 'logs', 'LOG_LEVEL': 'CRITICAL' })
process.crawl(Lifetech_Crawler)
process.start()  
