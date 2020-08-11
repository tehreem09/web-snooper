import scrapy


class LifetechCrawler(scrapy.Spider):
    name = "Lifetech"
    numbers = ['3216386601', '3408372640']
    custom_settings = {
        'FEED_URI': 'lifetech_rawdata.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORTERS': {
            'json': 'scrapy.exporters.JsonItemExporter',
        },
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    def start_requests(self):
        for i in self.numbers:
            urls = 'http://lifetech.tech/?number={}'.format(i)
            yield scrapy.Request(url=urls, callback=self.parse)

    def parse(self, response):
        for tr in response.css('table'):
            title = tr.xpath('//tr//td//strong/text()').extract()
            yield {'titlestext': title}
