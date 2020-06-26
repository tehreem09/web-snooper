import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider

# from scrapy import cmdline
#
# cmdline.execute("scrapy crawl myspider".split())
#
# Put that script in the same path where you put scrapy.cfg

class QuotesScraper(scrapy.Spider):
    name = "quotes_scraper"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        # response.css('tagname.classname::text')[item_no if required specific item].extract()
        # response.css('tagname#idname::text')[item_no if required specific item].extract()
        # response.xpath('//tag[@class='name']/text()')[same as above].extract()
        # response.xpath('//tag[@id='name']/text()')[same as above].extract()
        # response.css('tagname.classname tagname').xpath('@href').extract()
        title = response.css('title::text').extract_first()
        print(title)
        yield {"title": title}
        # yield "............"
        # print(".....", response, ".....")
        # yield title
        # all_quotes = response.css("div.quote span.text::text").extract()
        # all_authors = response.css("div.quote small.author::text").extract()
        # all_tags = response.css("div.quote div.tags a.tag::text").extract()
        # for quote, author, tag in list(zip(all_quotes, all_authors, all_tags)):
        #     # yield {
        #     #     'quote': quote,
        #     #     'author': author,
        #     #     'tag': tag
        #     # }
        #     print("..................................................................................")
        #     print(quote + "\n......." + author + "......." + tag)

        div_all = response.css("div.quote")
        for set in div_all:
            quote = set.css("span.text::text").extract_first()
            author = set.css("small.author::text").extract_first()
            tags = set.css("div.tags a.tag::text").extract()
            tags = ','.join(tags)
            yield {
                    'quote': quote,
                    'author': author,
                    'tag': tags
                }
            print(quote, "\n.......", author, ".......", tags)
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield {'page': next_page}
            yield response.follow(next_page, callback=self.parse)


# print("..............................................................................................")
# process = CrawlerProcess(settings={"FEEDS": {"item01.json": {"format": "json"}},
#                                    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
#                                    'LOG_FILE': 'logs',
#                                    'LOG_LEVEL': 'CRITICAL'})
# process.crawl(QuotesScraper)
# # prefs(ignore=Spider)
#
# print("........ before process.start() ........")
# process.start()

