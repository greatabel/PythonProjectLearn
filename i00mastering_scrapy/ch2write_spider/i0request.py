import scrapy

request = scrapy.Request('http://books.toscrape.com/')
# request2 = scrapy.Request('http://quotes.toscrape.com/', callback=self.parseItem)